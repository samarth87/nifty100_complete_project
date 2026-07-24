from pathlib import Path
import sqlite3,pandas as pd
from .ratios import compute
R=Path(__file__).resolve().parents[2]
def run():
 c=sqlite3.connect(R/'db/nifty100.db');q='SELECT c.company_id,c.broad_sector,p.year,p.sales,p.operating_profit,p.other_income,p.interest,p.net_profit,p.earnings_per_share,b.equity_capital,b.reserves,b.borrowings,b.total_assets,b.investments,f.operating_activity,f.investing_activity,f.financing_activity FROM companies c JOIN profitandloss p USING(company_id) LEFT JOIN balancesheet b ON b.company_id=p.company_id AND b.year=p.year LEFT JOIN cashflow f ON f.company_id=p.company_id AND f.year=p.year'
 d=pd.read_sql_query(q,c);rows=[]
 for r in d.to_dict('records'):
  x={'company_id':r['company_id'],'year':r['year']};x.update(compute(r));rows.append(x)
 if rows:pd.DataFrame(rows).to_sql('financial_ratios',c,if_exists='replace',index=False)
 c.close();print('rows',len(rows))
if __name__=='__main__':run()
