from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Nifty 100 Analytics", layout="wide", initial_sidebar_state="expanded")
ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "db" / "nifty100.db"


@st.cache_data(ttl=600)
def query(sql: str, params: tuple = ()) -> pd.DataFrame:
    with sqlite3.connect(DB) as conn:
        return pd.read_sql_query(sql, conn, params=params)


def safe_table(name: str) -> bool:
    result = query("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (name,))
    return not result.empty


def year_number(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.astype(str).str.extract(r"(\d{4})")[0], errors="coerce")


st.title("Nifty 100 Analytics")
page = st.sidebar.radio("Screen", ["Home", "Company Profile", "Screener", "Peers", "Trends", "Sectors", "Capital Allocation", "Reports"])

if not DB.exists():
    st.error("Database not found. Run: python -m src.etl.loader --init-db --load-all")
    st.stop()

if page == "Home":
    companies = query("SELECT c.*, s.broad_sector, s.sub_sector FROM companies c LEFT JOIN sectors s ON c.company_id=s.company_id")
    ratios = query("SELECT * FROM financial_ratios")
    market = query("SELECT * FROM market_cap")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Companies", len(companies))
    c2.metric("Average ROE", f"{ratios.return_on_equity_pct.mean():.1f}%" if not ratios.empty else "N/A")
    c3.metric("Median P/E", f"{market.pe_ratio.median():.1f}" if not market.empty else "N/A")
    c4.metric("Debt-Free Records", int((ratios.debt_to_equity == 0).sum()) if not ratios.empty else 0)
    if not companies.empty:
        sector_counts = companies.groupby("broad_sector", dropna=False).size().reset_index(name="companies")
        st.plotly_chart(px.pie(sector_counts, names="broad_sector", values="companies", hole=.45, title="Nifty 100 Sector Mix"), use_container_width=True)
        st.dataframe(companies[["company_id", "company_name", "broad_sector", "sub_sector", "roe_percentage", "roce_percentage"]], use_container_width=True, hide_index=True)
    else:
        st.warning("No companies loaded. Run the ETL command shown above.")

elif page == "Company Profile":
    choices = query("SELECT company_id, company_name FROM companies ORDER BY company_name")
    if choices.empty:
        st.warning("No companies loaded.")
        st.stop()
    labels = {f"{r.company_id} — {r.company_name}": r.company_id for r in choices.itertuples()}
    selected = st.selectbox("Company", list(labels), index=list(labels.values()).index("TCS") if "TCS" in labels.values() else 0)
    ticker = labels[selected]
    company = query("SELECT c.*, s.broad_sector, s.sub_sector FROM companies c LEFT JOIN sectors s ON c.company_id=s.company_id WHERE c.company_id=?", (ticker,))
    st.subheader(company.iloc[0]["company_name"])
    st.caption(f"{ticker} • {company.iloc[0].get('broad_sector', 'N/A')} • {company.iloc[0].get('sub_sector', 'N/A')}")
    st.write(company.iloc[0].get("about_company", ""))
    ratios = query("SELECT * FROM financial_ratios WHERE company_id=?", (ticker,))
    pl = query("SELECT * FROM profitandloss WHERE company_id=?", (ticker,))
    if not ratios.empty:
        ratios["year_num"] = year_number(ratios["year"])
        ratios = ratios.sort_values("year_num")
        latest = ratios.iloc[-1]
        cols = st.columns(5)
        metrics = [("ROE", "return_on_equity_pct", "%"), ("NPM", "net_profit_margin_pct", "%"), ("D/E", "debt_to_equity", ""), ("FCF", "free_cash_flow_cr", " Cr"), ("Asset Turnover", "asset_turnover", "")]
        for col, (label, field, suffix) in zip(cols, metrics):
            value = latest.get(field)
            col.metric(label, "N/A" if pd.isna(value) else f"{value:.2f}{suffix}")
        chart_cols = [c for c in ["return_on_equity_pct", "net_profit_margin_pct", "operating_profit_margin_pct"] if c in ratios.columns]
        st.plotly_chart(px.line(ratios, x="year_num", y=chart_cols, markers=True, title="Ratio Trends"), use_container_width=True)
    if not pl.empty:
        pl["year_num"] = year_number(pl["year"])
        pl = pl.sort_values("year_num")
        st.plotly_chart(px.bar(pl, x="year_num", y=["sales", "net_profit"], barmode="group", title="Revenue and Net Profit"), use_container_width=True)
    pc = query("SELECT pros, cons FROM prosandcons WHERE company_id=?", (ticker,))
    if not pc.empty:
        a, b = st.columns(2)
        a.success("Pros\n\n" + "\n\n".join("✓ " + str(x) for x in pc.pros.dropna()))
        b.error("Cons\n\n" + "\n\n".join("✗ " + str(x) for x in pc.cons.dropna()))

elif page == "Screener":
    latest = query("""
      SELECT r.*, c.company_name, s.broad_sector, m.pe_ratio, m.pb_ratio, m.dividend_yield_pct
      FROM financial_ratios r
      JOIN companies c ON c.company_id=r.company_id
      LEFT JOIN sectors s ON s.company_id=r.company_id
      LEFT JOIN market_cap m ON m.company_id=r.company_id
    """)
    if latest.empty:
        st.warning("No ratio data loaded.")
        st.stop()
    latest["year_num"] = year_number(latest["year"])
    latest = latest.sort_values("year_num").groupby("company_id", as_index=False).tail(1)
    min_roe = st.sidebar.slider("Minimum ROE %", -50.0, 100.0, 15.0)
    max_de = st.sidebar.slider("Maximum D/E", 0.0, 10.0, 2.0)
    min_fcf = st.sidebar.number_input("Minimum FCF (Cr)", value=0.0)
    result = latest[(latest.return_on_equity_pct >= min_roe) & (latest.debt_to_equity <= max_de) & (latest.free_cash_flow_cr >= min_fcf)]
    st.metric("Companies matching", len(result))
    st.dataframe(result[["company_id", "company_name", "broad_sector", "return_on_equity_pct", "debt_to_equity", "free_cash_flow_cr", "pe_ratio", "pb_ratio"]], use_container_width=True, hide_index=True)
    st.download_button("Download CSV", result.to_csv(index=False), "screener_results.csv", "text/csv")

elif page == "Peers":
    groups = query("SELECT DISTINCT peer_group_name FROM peer_groups ORDER BY peer_group_name")
    if groups.empty:
        st.warning("No peer groups loaded.")
        st.stop()

    group = st.selectbox("Peer group", groups["peer_group_name"].tolist())

    # Select columns explicitly. Do not use r.* because it adds another
    # company_id column and causes: Grouper for 'company_id' not 1-dimensional.
    peers = query("""
        SELECT
            p.peer_group_name,
            p.company_id,
            p.is_benchmark,
            c.company_name,
            r.year,
            r.return_on_equity_pct,
            r.net_profit_margin_pct,
            r.operating_profit_margin_pct,
            r.debt_to_equity,
            r.free_cash_flow_cr,
            r.revenue_cagr_5yr,
            r.pat_cagr_5yr,
            r.asset_turnover
        FROM peer_groups AS p
        JOIN companies AS c
            ON c.company_id = p.company_id
        LEFT JOIN financial_ratios AS r
            ON r.company_id = p.company_id
        WHERE p.peer_group_name = ?
    """, (group,))

    if peers.empty:
        st.warning("No company data found for this peer group.")
    else:
        # Extra safety: remove duplicate column names if the query is changed later.
        peers = peers.loc[:, ~peers.columns.duplicated()].copy()

        if "year" in peers.columns:
            peers["year_num"] = year_number(peers["year"])
            peers = (
                peers.sort_values("year_num")
                .groupby("company_id", as_index=False)
                .tail(1)
            )

        display_columns = [
            "company_id",
            "company_name",
            "is_benchmark",
            "return_on_equity_pct",
            "net_profit_margin_pct",
            "debt_to_equity",
            "free_cash_flow_cr",
        ]
        display_columns = [column for column in display_columns if column in peers.columns]

        st.dataframe(
            peers[display_columns],
            use_container_width=True,
            hide_index=True,
        )

elif page == "Trends":
    ticker = st.selectbox("Company", query("SELECT company_id FROM companies ORDER BY company_id").company_id.tolist())
    ratios = query("SELECT * FROM financial_ratios WHERE company_id=?", (ticker,))
    ratios["year_num"] = year_number(ratios["year"])
    available = [c for c in ["return_on_equity_pct", "net_profit_margin_pct", "operating_profit_margin_pct", "debt_to_equity", "asset_turnover"] if c in ratios]
    chosen = st.multiselect("Metrics", available, default=available[:2], max_selections=3)
    if chosen:
        st.plotly_chart(px.line(ratios.sort_values("year_num"), x="year_num", y=chosen, markers=True), use_container_width=True)

elif page == "Sectors":
    data = query("""
      SELECT s.*,c.company_name,r.return_on_equity_pct,r.net_profit_margin_pct,r.debt_to_equity,m.market_cap_crore
      FROM sectors s JOIN companies c ON c.company_id=s.company_id
      LEFT JOIN financial_ratios r ON r.company_id=s.company_id
      LEFT JOIN market_cap m ON m.company_id=s.company_id
    """)
    sector = st.selectbox("Sector", sorted(data.broad_sector.dropna().unique()))
    d = data[data.broad_sector == sector].drop_duplicates("company_id", keep="last")
    st.plotly_chart(px.scatter(d, x="market_cap_crore", y="return_on_equity_pct", size="market_cap_crore", hover_name="company_name", title=sector), use_container_width=True)
    st.dataframe(d, use_container_width=True, hide_index=True)

elif page == "Capital Allocation":
    cf = query("SELECT * FROM cashflow")
    if cf.empty:
        st.warning("No cash-flow data loaded.")
        st.stop()
    def pattern(r):
        signs = tuple("+" if r[c] >= 0 else "-" for c in ["operating_activity", "investing_activity", "financing_activity"])
        return {("+","-","-"):"Reinvestor", ("+","+","-"):"Liquidating Assets", ("-","+","+"):"Distress Signal", ("-","-","+"):"Growth Funded by Debt", ("+","+","+"):"Cash Accumulator", ("-","-","-"):"Pre-Revenue", ("+","-","+"):"Mixed"}.get(signs, "Other")
    cf["pattern"] = cf.apply(pattern, axis=1)
    cf["year_num"] = year_number(cf["year"])
    latest = cf.sort_values("year_num").groupby("company_id", as_index=False).tail(1)
    counts = latest.groupby("pattern").size().reset_index(name="companies")
    st.plotly_chart(px.treemap(counts, path=["pattern"], values="companies", title="Latest Capital Allocation Patterns"), use_container_width=True)
    st.dataframe(latest[["company_id", "year", "operating_activity", "investing_activity", "financing_activity", "pattern"]], use_container_width=True, hide_index=True)

elif page == "Reports":
    docs = query("SELECT d.*,c.company_name FROM documents d LEFT JOIN companies c ON c.company_id=d.company_id ORDER BY company_id,year DESC")
    ticker = st.selectbox("Company", sorted(docs.company_id.unique())) if not docs.empty else None
    if ticker:
        selected = docs[docs.company_id == ticker]
        for row in selected.itertuples():
            st.markdown(f"**{row.year}** — [Open annual report]({row.annual_report})")