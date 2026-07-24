from src.etl.normaliser import normalize_year,normalize_ticker
def test_year():assert normalize_year('FY 2024')==2024
def test_ticker():assert normalize_ticker('NSE:TCS.NS')=='TCS'
