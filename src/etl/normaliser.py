import re
import pandas as pd
def normalize_year(v):
 if pd.isna(v): return None
 if hasattr(v,'year'): return int(v.year)
 y=re.findall(r'(?:19|20)\d{2}',str(v)); return int(y[-1]) if y else None
def normalize_ticker(v):
 if pd.isna(v): return None
 s=str(v).strip().upper();s=re.sub(r'^(NSE:|BSE:)','',s);s=re.sub(r'\.(NS|BO)$','',s);return re.sub(r'[^A-Z0-9&-]','',s)
def snake(v): return re.sub(r'_+','_',re.sub(r'[^a-z0-9]+','_',str(v).strip().lower())).strip('_')
