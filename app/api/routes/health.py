from fastapi import APIRouter

router = APIRouter()

# Health check endpoint - verifica o status do serviço
@router.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "duckdb-analytics-api"
    }
