import pytest
import duckdb
from app.services import analytics_service

@pytest.fixture(scope="session")
def duckdb_test_conn():
    conn = duckdb.connect(":memory:")

    conn.execute("""
        CREATE TABLE sales (
            id INTEGER,
            total_amount DOUBLE,
            created_at DATE
        )
    """)

    conn.execute("""
        INSERT INTO sales VALUES
        (1, 100.0, '2023-01-01'),
        (2, 200.0, '2023-01-02')
    """)

    yield conn
    conn.close()


@pytest.fixture(autouse=True)
def override_db_connection(monkeypatch, duckdb_test_conn):
    monkeypatch.setattr(
        analytics_service,
        "get_connection",
        lambda: duckdb_test_conn
    )
