from fastapi.testclient import TestClient
from src.api.main import app
def test_health():assert TestClient(app).get('/api/v1/health').status_code==200
