from fastapi import APIRouter
from app.core.database import get_connection

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def health_check():
    conn = get_connection()
    conn.execute("SELECT 1")
    return {
        "status": "ok",
        "database": "duckdb",
    }
