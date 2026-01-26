import duckdb
import pytest

@pytest.fixture
def duckdb_conn():
    conn = duckdb.connect(":memory:")
    conn.execute("""
        CREATE TABLE sales (
            created_at DATE,
            total_amount DOUBLE
        )
    """)
    conn.execute("""
        INSERT INTO sales VALUES
        ('2023-01-01', 100.0),
        ('2023-01-02', 200.0)
    """)
    return conn
