from src.analytics.ratios import compute
def test_debt_free():assert compute({'borrowings':0,'equity_capital':10,'reserves':20})['debt_to_equity']==0
def test_negative_equity():assert compute({'borrowings':10,'equity_capital':-20,'reserves':0,'net_profit':3})['return_on_equity_pct'] is None
