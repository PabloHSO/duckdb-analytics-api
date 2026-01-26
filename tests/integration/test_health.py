from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ----------------------------------------
# Teste do endpoint de healthcheck 
# ----------------------------------------
def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["database"] == "ok"