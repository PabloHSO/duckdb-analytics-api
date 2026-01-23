from fastapi import APIRouter
from app.services.query_service import get_top_users
from app.schemas.query import TopUserResponse
from typing import List

router = APIRouter(prefix="/queries", tags=["Queries"])

@router.get("/top-users", response_model=List[TopUserResponse])
def top_users(limit: int = 5):
    return get_top_users(limit)
