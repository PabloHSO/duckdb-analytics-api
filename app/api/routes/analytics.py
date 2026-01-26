from fastapi import APIRouter, Query
from datetime import date
from typing import List

from app.services.analytics_service import AnalyticsService
from app.schemas.analytics import (
    DailySales,
    MonthlyRevenue,
    TotalRevenueResponse,
    RevenueByDayItem,
    TopUserItem,
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/daily-sales", response_model=List[DailySales])
def daily_sales():
    return AnalyticsService.get_daily_sales()


@router.get("/monthly-revenue", response_model=List[MonthlyRevenue])
def monthly_revenue():
    return AnalyticsService.get_monthly_revenue()


@router.get("/revenue", response_model=TotalRevenueResponse)
def total_revenue(
    start_date: date | None = Query(None),
    end_date: date | None = Query(None),
):
    total = AnalyticsService.total_revenue(start_date, end_date)
    return {"total_revenue": total}


@router.get("/revenue/daily", response_model=List[RevenueByDayItem])
def revenue_by_day():
    return AnalyticsService.revenue_by_day()


@router.get("/top-users", response_model=List[TopUserItem])
def top_users(limit: int = 5):
    return AnalyticsService.top_users(limit)
