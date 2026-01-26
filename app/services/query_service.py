from app.core.database import get_connection # Importa a função para obter a conexão com o banco de dados DuckDB

# Função para obter os principais usuários por gasto total
def get_top_users(limit: int = 5):
    conn = get_connection()

    # Executa a consulta SQL para agregar os gastos por usuário e ordenar em ordem decrescente
    result = conn.execute(f"""
        SELECT
            user_id,
            SUM(total_amount) AS total_spent
        FROM sales
        GROUP BY user_id
        ORDER BY total_spent DESC
        LIMIT {limit}
    """).fetchall() # Busca todos os resultados da consulta

    return [
        {"user_id": row[0], "total_spent": row[1]}
        for row in result
    ]

ALLOWED_METRICS = {
    "total_sales": "SELECT SUM(total_amount) FROM sales",
    "avg_ticket": "SELECT AVG(total_amount) FROM sales",
    "orders_count": "SELECT COUNT(*) FROM sales"
}

def run_metric(metric: str, start_date=None, end_date=None) -> float:
    if metric not in ALLOWED_METRICS:
        raise ValueError("Metrica inválida")

    base_query = ALLOWED_METRICS[metric]
    filters = []

    if start_date:
        filters.append(f"created_at >= DATE '{start_date}'")
    if end_date:
        filters.append(f"created_at <= DATE '{end_date}'")

    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    conn = get_connection()
    result = conn.execute(base_query).fetchone()

    return result[0] or 0