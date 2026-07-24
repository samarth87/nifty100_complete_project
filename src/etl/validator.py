import pandas as pd
def validate_tables(t):
 out=[]
 for name,d in t.items():
  if 'company_id' in d and d.company_id.isna().any():out.append(['DQ-01',None,'company_id',f'Null key in {name}','CRITICAL'])
  if {'company_id','year'}<=set(d.columns) and d.duplicated(['company_id','year']).any():out.append(['DQ-02',None,'company_id,year',f'Duplicate key in {name}','CRITICAL'])
 pl=t.get('profitandloss',pd.DataFrame())
 if not pl.empty and 'sales' in pl:
  for _,r in pl[pl.sales.fillna(0)<=0].iterrows():out.append(['DQ-06',r.get('company_id'),'sales','Non-positive sales','WARNING'])
 return pd.DataFrame(out,columns=['rule_id','company_id','field','issue','severity'])
