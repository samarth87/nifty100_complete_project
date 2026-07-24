from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
DB = ROOT / "db" / "nifty100.db"
OUTPUT = ROOT / "output"

FILE_TABLES = {
    "companies": "companies",
    "sectors": "sectors",
    "profitandloss": "profitandloss",
    "balancesheet": "balancesheet",
    "cashflow": "cashflow",
    "analysis": "analysis",
    "documents": "documents",
    "prosandcons": "prosandcons",
    "peer_groups": "peer_groups",
    "stock_prices": "stock_prices",
    "financial_ratios": "financial_ratios",
    "market_cap": "market_cap",
}


def clean_name(value: object) -> str:
    return (
        str(value).strip().lower().replace("&", "and").replace("/", "_")
        .replace(" ", "_").replace("-", "_").replace("%", "pct")
    )


def read_excel_clean(path: Path) -> pd.DataFrame:
    """Read files that may contain a decorative first row above the real headers."""
    preview = pd.read_excel(path, header=None, nrows=3)
    first = [str(x).strip().lower() for x in preview.iloc[0].tolist()]
    second = [str(x).strip().lower() for x in preview.iloc[1].tolist()] if len(preview) > 1 else []
    known = {"id", "company_id", "year", "date", "peer_group_name"}
    header_row = 1 if not known.intersection(first) and known.intersection(second) else 0
    df = pd.read_excel(path, header=header_row)
    df.columns = [clean_name(c) for c in df.columns]
    df = df.dropna(how="all")
    return df


def init_db() -> None:
    DB.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB) as conn:
        conn.executescript((ROOT / "db" / "schema.sql").read_text(encoding="utf-8"))


def load_all() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    audit: list[dict] = []
    with sqlite3.connect(DB) as conn:
        for stem, table in FILE_TABLES.items():
            matches = sorted(RAW.glob(f"{stem}*.xlsx"))
            if not matches:
                audit.append({"table": table, "rows_loaded": 0, "status": "FILE MISSING"})
                continue
            path = matches[0]
            try:
                df = read_excel_clean(path)
                # Source-to-database column corrections.
                df = df.rename(columns={
                    "annual_report": "annual_report",
                    "dividend_payout": "dividend_payout",
                })
                allowed = [row[1] for row in conn.execute(f"PRAGMA table_info({table})")]
                use = [c for c in df.columns if c in allowed]
                if "company_id" in df.columns:
                    df["company_id"] = df["company_id"].astype(str).str.strip().str.upper()
                if table == "companies":
                    if "company_id" not in df.columns and "id" in df.columns:
                        df = df.rename(columns={"id": "company_id"})
                    df["company_id"] = df["company_id"].astype(str).str.strip().str.upper()
                if "is_benchmark" in df.columns:
                    df["is_benchmark"] = df["is_benchmark"].fillna(False).astype(bool).astype(int)
                use = [c for c in df.columns if c in allowed]
                df = df[use]
                pk_cols = [row[1] for row in conn.execute(f"PRAGMA table_info({table})") if row[5] > 0]
                if pk_cols:
                    df = df.drop_duplicates(subset=pk_cols, keep="last")
                else:
                    df = df.drop_duplicates()
                df.to_sql(table, conn, if_exists="append", index=False)
                audit.append({"table": table, "rows_loaded": len(df), "status": "OK", "file": path.name})
            except Exception as exc:
                audit.append({"table": table, "rows_loaded": 0, "status": f"ERROR: {exc}", "file": path.name})
        conn.commit()
    pd.DataFrame(audit).to_csv(OUTPUT / "load_audit.csv", index=False)
    print(pd.DataFrame(audit).to_string(index=False))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--init-db", action="store_true")
    parser.add_argument("--load-all", action="store_true")
    args = parser.parse_args()
    if args.init_db:
        init_db()
    if args.load_all:
        load_all()


if __name__ == "__main__":
    main()
