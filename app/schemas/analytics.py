from pydantic import BaseModel
from datetime import date

class DailySales(BaseModel):
    date: date
    total_sales: float
    orders: int

class TopUser(BaseModel):
    user_id: int
    total_spent: float

class MonthlyRevenue(BaseModel):
    month: str
    revenue: float

class TotalRevenueResponse(BaseModel):
    total_revenue: float

class RevenueByDayItem(BaseModel):
    date: date
    revenue: float

class TopUserItem(BaseModel):
    user_id: int
    total_spent: float

class KPISummary(BaseModel):
    total_revenue: float
    total_orders: int
    average_ticket: float
    unique_users: int


class CumulativeRevenueItem(BaseModel):
    date: date
    cumulative_revenue: float


class MonthlyComparison(BaseModel):
    month: str
    revenue: float
    previous_month_revenue: float | None
    growth_percentage: float | None