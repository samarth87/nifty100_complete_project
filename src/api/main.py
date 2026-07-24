from fastapi import FastAPI,HTTPException
import sqlite3,time
from pathlib import Path
DB=Path(__file__).resolve().parents[2]/'db/nifty100.db';app=FastAPI(title='Nifty 100 API',version='1.0.0');START=time.time()
def rows(q,p=()):
 with sqlite3.connect(DB) as c:
  c.row_factory=sqlite3.Row;return [dict(x) for x in c.execute(q,p).fetchall()]
@app.get('/api/v1/health')
def health():
 tables=['companies','profitandloss','balancesheet','cashflow','stock_prices','financial_ratios','peer_groups','peer_percentiles','documents','sectors'];counts={}
 for t in tables:
  try:counts[t]=rows(f'SELECT COUNT(*) n FROM {t}')[0]['n']
  except Exception:counts[t]=0
 return {'status':'ok','db_row_counts':counts,'uptime_seconds':round(time.time()-START,2),'version':'1.0.0'}
@app.get('/api/v1/companies')
def companies(sector:str|None=None,search:str|None=None):
 q='SELECT * FROM companies WHERE 1=1';p=[]
 if sector:q+=' AND broad_sector=?';p.append(sector)
 if search:q+=' AND (company_name LIKE ? OR ticker LIKE ?)';p += [f'%{search}%',f'%{search}%']
 return rows(q,p)
@app.get('/api/v1/companies/{ticker}')
def company(ticker:str):
 r=rows('SELECT * FROM companies WHERE ticker=?',(ticker.upper(),))
 if not r:raise HTTPException(404,'Ticker not found')
 return r[0]
@app.get('/api/v1/companies/{ticker}/ratios')
def ratios(ticker:str,year:int|None=None):
 q='SELECT * FROM financial_ratios WHERE company_id=?';p=[ticker.upper()]
 if year:q+=' AND year=?';p.append(year)
 return rows(q,p)
@app.get('/api/v1/sectors')
def sectors():return rows('SELECT broad_sector,COUNT(*) company_count FROM companies GROUP BY broad_sector')
@app.get('/api/v1/screener')
def screener(min_roe:float|None=None,max_de:float|None=None):
 q='SELECT c.*,r.* FROM companies c JOIN financial_ratios r USING(company_id) WHERE r.year=(SELECT MAX(year) FROM financial_ratios)';p=[]
 if min_roe is not None:q+=' AND return_on_equity_pct>=?';p.append(min_roe)
 if max_de is not None:q+=' AND (broad_sector="Financials" OR debt_to_equity<=?)';p.append(max_de)
 return rows(q,p)
