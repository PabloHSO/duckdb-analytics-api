from pathlib import Path
from app.core.database import get_connection


class DatasetService:

    @staticmethod
    def ingest_sales() -> dict:
        """
        Ingestão padrão do dataset de vendas (demo).
        """
        csv_path = Path("data/samples/sales.csv")
        conn = get_connection()

        conn.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                order_id INTEGER,
                user_id INTEGER,
                amount DOUBLE,
                created_at DATE
            )
        """)

        conn.execute(f"""
            INSERT INTO sales
            SELECT * FROM read_csv_auto('{csv_path}')
        """)

        return {"status": "sales dataset ingested successfully"}

    @staticmethod
    def load_csv_as_table(table_name: str, file_path: str) -> int:
        """
        Carrega qualquer CSV como tabela DuckDB.
        """
        conn = get_connection()

        conn.execute(f"""
            CREATE OR REPLACE TABLE {table_name} AS
            SELECT * FROM read_csv_auto('{file_path}')
        """)

        rows = conn.execute(
            f"SELECT COUNT(*) FROM {table_name}"
        ).fetchone()[0]

        return rows
