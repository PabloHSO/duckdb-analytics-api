from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

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
    assert "total_revenue" in response.json()
    assert isinstance(response.json()["total_revenue"], float)

def test_total_revenue_with_dates():
    response = client.get("/analytics/revenue?start_date=2023-01-01&end_date=2023-12-31")
    assert response.status_code == 200
    assert "total_revenue" in response.json()
    assert isinstance(response.json()["total_revenue"], float)