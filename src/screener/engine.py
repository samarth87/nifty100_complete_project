def apply_filters(d,**f):
 x=d.copy();m={'min_roe':'return_on_equity_pct','max_de':'debt_to_equity','min_fcf':'free_cash_flow_cr','min_rev_cagr_5yr':'revenue_cagr_5yr','min_pat_cagr_5yr':'pat_cagr_5yr','max_pe':'pe'}
 for k,v in f.items():
  c=m.get(k)
  if c in x and v is not None:x=x[x[c]>=v] if k.startswith('min_') else x[x[c]<=v]
 return x
