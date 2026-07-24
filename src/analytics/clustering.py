from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
def run(d):
 feats=['return_on_equity_pct','debt_to_equity','revenue_cagr_5yr','fcf_cagr_5yr','operating_profit_margin_pct']
 for c in feats:d[c]=d[c].fillna(d.groupby('broad_sector')[c].transform('median')).fillna(d[c].median())
 X=StandardScaler().fit_transform(d[feats]);m=KMeans(5,random_state=42,n_init=20).fit(X);d['cluster_id']=m.labels_;return d
