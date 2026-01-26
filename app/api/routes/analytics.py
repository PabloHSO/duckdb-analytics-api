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
    KPISummary,
    CumulativeRevenueItem,
    MonthlyComparison,
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/daily-sales", response_model=List[DailySales])
def daily_sales():
    '''
    Retorna as vendas diárias agregadas.
    '''
    return AnalyticsService.get_daily_sales()


@router.get("/monthly-revenue", response_model=List[MonthlyRevenue])
def monthly_revenue():
    '''
    Retorna a receita mensal agregada.
    '''
    return AnalyticsService.get_monthly_revenue()


@router.get("/revenue", response_model=TotalRevenueResponse)
def total_revenue(
    start_date: date | None = Query(None),
    end_date: date | None = Query(None),
):
    '''
    Retorna a receita total em um intervalo de datas.
    '''
    total = AnalyticsService.total_revenue(start_date, end_date)
    return {"total_revenue": total}


@router.get("/revenue/daily", response_model=List[RevenueByDayItem])
def revenue_by_day():
    '''
    Retorna a receita diária.
    '''
    return AnalyticsService.revenue_by_day()

@router.get("/top-users", response_model=List[TopUserItem])
def top_users(limit: int = 5):
    '''
    Retorna os principais usuários por gasto.
    '''
    return AnalyticsService.top_users(limit)

@router.get("/kpis", response_model=KPISummary)
def kpis():
    '''
    Retorna o resumo dos KPIs.
    '''
    return AnalyticsService.kpi_summary()

@router.get("/revenue/cumulative", response_model=list[CumulativeRevenueItem],)
def cumulative_revenue():
    '''
    Retorna a receita acumulada ao longo do tempo.
    '''
    return AnalyticsService.cumulative_revenue()


@router.get("/revenue/monthly-comparison", response_model=list[MonthlyComparison],)
def monthly_comparison():
    '''
    Retorna a comparação da receita mensal com o mês anterior.
    '''
    return AnalyticsService.monthly_comparison()