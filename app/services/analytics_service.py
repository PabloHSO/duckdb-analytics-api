from app.core.database import get_connection
from typing import List, Dict
from datetime import date

class AnalyticsService:

    @staticmethod
    def daily_sales() -> List[Dict]:
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

        return [
            {"user_id": r[0], "total_spent": r[1]}
            for r in rows
        ]

    @staticmethod
    def monthly_revenue() -> List[Dict]:
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

        return [
            {"month": r[0], "revenue": r[1]}
            for r in rows
        ]

    @staticmethod
    def total_revenue(
        start_date: date | None = None,
        end_date: date | None = None
    ) -> float:
        conn = get_connection()

        query = "SELECT SUM(total_amount) FROM sales"
        params = []

        if start_date and end_date:
            query += " WHERE created_at BETWEEN ? AND ?"
            params = [start_date, end_date]

        result = conn.execute(query, params).fetchone()
        return float(result[0] or 0)

    @staticmethod
    def revenue_by_day() -> List[Dict]:
        conn = get_connection()
        query = """
            SELECT created_at, SUM(total_amount) AS revenue
            FROM sales
            GROUP BY created_at
            ORDER BY created_at
        """
        rows = conn.execute(query).fetchall()

        return [{"date": r[0], "revenue": r[1]} for r in rows]
