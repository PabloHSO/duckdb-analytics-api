from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

# ----------------------------------------
# Teste do endpoint de load dataset 
# ----------------------------------------
def test_load_dataset_endpoint():
    table_name = f"test_table_{uuid.uuid4().hex[:8]}"

    payload = {
        "name": table_name,
        "path": "tests/data/sample.csv"
    }

    response = client.post("/datasets/load", json=payload)
    assert response.status_code == 200
    assert response.json()["table"] == table_name