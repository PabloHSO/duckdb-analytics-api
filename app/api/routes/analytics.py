from fastapi import APIRouter, Query
from datetime import date
from typing import List
from app.services.analytics_service import AnalyticsService
from app.schemas.analytics import (
    DailySales,
    TopUser,
    MonthlyRevenue,
    TotalRevenueResponse,
    RevenueByDayItem
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/daily-sales", response_model=List[DailySales])
def daily_sales():
    """
    Retorna as vendas diárias, incluindo total e número de pedidos.
    """
    return AnalyticsService.daily_sales()


@router.get("/top-users", response_model=List[TopUser])
def top_users(limit: int = 5):
    """
    Retorna os usuários com maior gasto.
    """
    return AnalyticsService.top_users(limit)


@router.get("/monthly-revenue", response_model=List[MonthlyRevenue])
def monthly_revenue():
    """
    Retorna a receita agregada por mês.
    """
    return AnalyticsService.monthly_revenue()


@router.get("/revenue", response_model=TotalRevenueResponse)
def get_total_revenue(
    start_date: date | None = Query(None),
    end_date: date | None = Query(None),
):
    '''
    Retorna a receita total dentro de um intervalo de datas.
    '''
    total = AnalyticsService.total_revenue(start_date, end_date)
    return {"total_revenue": total}


@router.get("/revenue/daily", response_model=List[RevenueByDayItem])
def get_daily_revenue():
    '''
    Retorna a receita diária dentro de um intervalo de datas.
    '''
    return AnalyticsService.revenue_by_day()
