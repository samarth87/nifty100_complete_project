from pathlib import Path
import pandas as pd
R=Path(__file__).resolve().parents[1];rows=[]
for f in (R/'data/raw').glob('*'):
 try:
  if f.suffix.lower() in ['.xlsx','.xls']:
   for s,d in pd.read_excel(f,sheet_name=None).items():rows.append([f.name,s,len(d),' | '.join(map(str,d.columns))])
  elif f.suffix.lower()=='.csv':
   d=pd.read_csv(f);rows.append([f.name,'CSV',len(d),' | '.join(map(str,d.columns))])
 except Exception as e:rows.append([f.name,'ERROR',0,str(e)])
pd.DataFrame(rows,columns=['file','sheet','rows','columns']).to_csv(R/'output/source_inventory.csv',index=False)
