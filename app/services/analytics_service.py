from app.core.database import get_connection
from typing import List, Dict
from datetime import date


class AnalyticsService:

    # Função para obter vendas diárias
    @staticmethod
    def get_daily_sales() -> List[Dict]:
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
        rows = conn.execute(query).fetchall()
        return [
            {"date": r[0], "total_sales": r[1], "orders": r[2]}
            for r in rows
        ]

    # Função para obter receita mensal
    @staticmethod
    def get_monthly_revenue() -> List[Dict]:
        conn = get_connection()
        query = """
            SELECT
                strftime('%Y-%m', created_at) AS month,
                SUM(total_amount) AS revenue
            FROM sales
            GROUP BY month
            ORDER BY month
        """
        rows = conn.execute(query).fetchall()
        return [{"month": r[0], "revenue": r[1]} for r in rows]

    # Função para calcular receita total em um intervalo de datas
    @staticmethod
    def total_revenue(
        start_date: date | None = None,
        end_date: date | None = None,
    ) -> float:
        conn = get_connection()

        query = "SELECT SUM(total_amount) FROM sales"
        params = []

        if start_date and end_date:
            query += " WHERE created_at BETWEEN ? AND ?"
            params = [start_date, end_date]

        result = conn.execute(query, params).fetchone()
        return float(result[0] or 0)

    # Função para obter receita diária
    @staticmethod
    def revenue_by_day() -> List[Dict]:
        conn = get_connection()
        query = """
            SELECT
                created_at AS date,
                SUM(total_amount) AS revenue
            FROM sales
            GROUP BY created_at
            ORDER BY created_at
        """
        rows = conn.execute(query).fetchall()
        return [{"date": r[0], "revenue": r[1]} for r in rows]

    # Função para obter os principais usuários por gasto
    @staticmethod
    def top_users(limit: int = 5) -> List[Dict]:
        conn = get_connection()
        query = """
            SELECT
                user_id,
                SUM(total_amount) AS total_spent
            FROM sales
            GROUP BY user_id
            ORDER BY total_spent DESC
            LIMIT ?
        """
        rows = conn.execute(query, [limit]).fetchall()
        return [{"user_id": r[0], "total_spent": r[1]} for r in rows]

    # Função para obter resumo de KPIs
    @staticmethod
    def kpi_summary():
        conn = get_connection()

        query = """
            SELECT
                SUM(total_amount) AS total_revenue,
                COUNT(*) AS total_orders,
                AVG(total_amount) AS average_ticket,
                COUNT(DISTINCT user_id) AS unique_users
            FROM sales
        """
        row = conn.execute(query).fetchone()

        return {
            "total_revenue": float(row[0] or 0),
            "total_orders": row[1],
            "average_ticket": float(row[2] or 0),
            "unique_users": row[3],
        }

    # Função para obter receita acumulada ao longo do tempo
    @staticmethod
    def cumulative_revenue():
        conn = get_connection()

        query = """
            SELECT
                created_at,
                SUM(SUM(total_amount)) OVER (ORDER BY created_at) AS cumulative_revenue
            FROM sales
            GROUP BY created_at
            ORDER BY created_at
        """
        rows = conn.execute(query).fetchall()

        return [
            {"date": r[0], "cumulative_revenue": r[1]}
            for r in rows
        ]

    # Função para comparar receita mensal com o mês anterior
    @staticmethod
    def monthly_comparison():
        # LAG - Função de janela SQL para acessar a linha anterior
        # OVER - Define a janela para a função de janela
        conn = get_connection()

        query = """
            WITH monthly AS (
                SELECT
                    strftime('%Y-%m', created_at) AS month,
                    SUM(total_amount) AS revenue
                FROM sales
                GROUP BY month
            )
            SELECT
                month,
                revenue,
                LAG(revenue) OVER (ORDER BY month) AS previous_month_revenue,
                CASE
                    WHEN LAG(revenue) OVER (ORDER BY month) IS NULL THEN NULL
                    ELSE ROUND(
                        ((revenue - LAG(revenue) OVER (ORDER BY month))
                        / LAG(revenue) OVER (ORDER BY month)) * 100, 2
                    )
                END AS growth_percentage
            FROM monthly
            ORDER BY month
        """

        rows = conn.execute(query).fetchall()

        return [
            {
                "month": r[0],
                "revenue": r[1],
                "previous_month_revenue": r[2],
                "growth_percentage": r[3],
            }
            for r in rows
        ]