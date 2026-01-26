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
