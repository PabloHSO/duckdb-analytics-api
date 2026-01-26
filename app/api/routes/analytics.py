from fastapi import APIRouter
from app.services.analytics_service import (
    get_daily_sales,
    get_top_users,
    get_monthly_revenue
)
from app.schemas.analytics import DailySales, TopUser, MonthlyRevenue
from typing import List

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/daily-sales", response_model=List[DailySales])
def daily_sales():
    '''
    Retorna as vendas diárias, incluindo a data, o total de vendas e o número de pedidos.
    '''
    rows = get_daily_sales()
    return [
        {"date": r[0], "total_sales": r[1], "orders": r[2]}
        for r in rows
    ]


@router.get("/top-users", response_model=List[TopUser])
def top_users(limit: int = 5):
    '''
    Retorna os principais usuários com base no gasto total.
    '''
    rows = get_top_users(limit)
    return [
        {"user_id": r[0], "total_spent": r[1]}
        for r in rows
    ]


@router.get("/monthly-revenue", response_model=List[MonthlyRevenue])
def monthly_revenue():
    '''
    Retorna a receita mensal agregada.
    '''
    rows = get_monthly_revenue()
    return [
        {"month": r[0], "revenue": r[1]}
        for r in rows
    ]
