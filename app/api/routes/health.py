from fastapi import APIRouter
from app.core.database import get_connection

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
# Pronto para Kubernetes / Load Balancer healthchecks
def healthcheck():
    try:
        conn = get_connection()
        conn.execute("SELECT 1")
        db_status = "ok"
    except Exception:
        db_status = "error"

    return {
        "status": "ok",
        "database": db_status,
    }