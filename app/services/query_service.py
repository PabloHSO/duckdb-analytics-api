from app.core.database import get_connection # Importa a função para obter a conexão com o banco de dados DuckDB

# Função para obter os principais usuários por gasto total
def get_top_users(limit: int = 5):
    conn = get_connection()

    # Executa a consulta SQL para agregar os gastos por usuário e ordenar em ordem decrescente
    result = conn.execute(f"""
        SELECT
            user_id,
            SUM(amount) AS total_spent
        FROM sales
        GROUP BY user_id
        ORDER BY total_spent DESC
        LIMIT {limit}
    """).fetchall() # Busca todos os resultados da consulta

    return [
        {"user_id": row[0], "total_spent": row[1]}
        for row in result
    ]
