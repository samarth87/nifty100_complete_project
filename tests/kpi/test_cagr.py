from src.analytics.cagr import calculate_cagr
def test_normal():assert round(calculate_cagr(100,121,2)[0],2)==10
def test_turnaround():assert calculate_cagr(-10,10,5)[1]=='TURNAROUND'
