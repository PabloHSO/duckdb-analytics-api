from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ingest_datasets_endpoint():
    response = client.post("/datasets/ingest")
    assert response.status_code == 200
    assert response.json()["message"] == "Datasets ingested successfully"  

def test_load_dataset_endpoint():
    payload = {
        "name": "test_table",
        "path": "tests/data/sample.csv"
    }
    
    response = client.post("/datasets/load", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Dataset carregado com sucesso"
    assert response.json()["table"] == "test_table"
    assert response.json()["rows_loaded"] > 0