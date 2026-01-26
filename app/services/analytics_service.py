from app.core.database import get_connection

# Função para obter vendas diárias
def get_daily_sales():
    conn = get_connection()
    query = """
        SELECT
            created_at AS date,
            SUM(total_amount) AS total_sales,
            COUNT(*) AS orders
        FROM sales
        GROUP BY created_at
        ORDER BY created_at
    """
    return conn.execute(query).fetchall()

# Função para obter os principais usuários por gasto total
def get_top_users(limit: int = 5):
    conn = get_connection()
    query = f"""
        SELECT
            user_id,
            SUM(total_amount) AS total_spent
        FROM sales
        GROUP BY user_id
        ORDER BY total_spent DESC
        LIMIT {limit}
    """
    return conn.execute(query).fetchall()

# Função para obter receita mensal
def get_monthly_revenue():
    conn = get_connection()
    query = """
        SELECT
            strftime('%Y-%m', created_at) AS month,
            SUM(total_amount) AS revenue
        FROM sales
        GROUP BY month
        ORDER BY month
    """
    return conn.execute(query).fetchall()
