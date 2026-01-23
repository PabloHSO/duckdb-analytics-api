from pathlib import Path
from app.core.database import get_connection

# Define o caminho do arquivo CSV de vendas
CSV_PATH = Path("data/samples/sales.csv")

# Função para ingerir o dataset de vendas no banco de dados DuckDB
def ingest_sales():
    conn = get_connection() # Obtém a conexão com o banco de dados DuckDB

    # Cria a tabela de vendas se não existir
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            order_id INTEGER,
            user_id INTEGER,
            amount DOUBLE,
            created_at DATE
        )
    """)

    # Ingesta os dados do arquivo CSV na tabela de vendas
    conn.execute(f"""
        INSERT INTO sales
        SELECT * FROM read_csv_auto('{CSV_PATH}')
    """)

    return {"status": "sales dataset ingested successfully"}
