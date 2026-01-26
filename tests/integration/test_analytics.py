from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ----------------------------------------
# Teste de endpoints de Analytics
# ----------------------------------------
def test_daily_sales_endpoint():
    response = client.get("/analytics/daily-sales")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_monthly_revenue_endpoint():
    response = client.get("/analytics/monthly-revenue")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_total_revenue_endpoint():
    response = client.get("/analytics/revenue")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "total_revenue" in data
    assert isinstance(data["total_revenue"], float)
