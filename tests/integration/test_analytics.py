from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ----------------------------------------
# Teste - Retorna as vendas diárias agregadas. 
# ----------------------------------------
def test_daily_sales_endpoint():
    response = client.get("/analytics/daily-sales")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    if data:
        assert "date" in data[0]
        assert "total_sales" in data[0]
        assert "orders" in data[0]

# ----------------------------------------
# Teste - Retorna a receita mensal agregada.
# ----------------------------------------
def test_monthly_revenue_endpoint():
    response = client.get("/analytics/monthly-revenue")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "month" in data[0]
        assert "total_revenue" in data[0]

# ----------------------------------------
# Teste - Retorna a receita total em um intervalo de datas.
# ----------------------------------------
def test_total_revenue_endpoint():
    response = client.get("/analytics/revenue")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "total_revenue" in data


# ----------------------------------------
# Teste - Retorna a receita total em um intervalo de datas com parâmetros.
# ----------------------------------------
def test_total_revenue_with_dates():
    response = client.get("/analytics/revenue?start_date=2023-01-01&end_date=2023-12-31")
    assert response.status_code == 200
    data = response.json()
    assert "total_revenue" in data