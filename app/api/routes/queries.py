from fastapi import APIRouter, HTTPException
from app.services.query_service import get_top_users
from app.schemas.query import TopUserResponse, QueryRequest, QueryResponse
from app.services.query_service import run_metric
from typing import List

router = APIRouter(prefix="/queries", tags=["Queries"])

@router.get("/top-users", response_model=List[TopUserResponse])
def top_users(limit: int = 5):
    return get_top_users(limit)

@router.post("/", response_model=QueryResponse)
def query_metrics(payload: QueryRequest):
    try:
        '''
        Executa a métrica solicitada com os parâmetros fornecidos.
        '''
        result = run_metric(
            metric=payload.metric,
            start_date=payload.start_date,
            end_date=payload.end_date
        )
        return {
            "metric": payload.metric,
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
