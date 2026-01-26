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