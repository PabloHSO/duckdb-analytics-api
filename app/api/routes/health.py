from fastapi import APIRouter
from app.core.database import get_connection

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def health_check():
    '''
    Verifica a saúde da API e a conectividade com o banco de dados DuckDB.
    Retorna um status "ok" se a conexão for bem-sucedida.
    '''
    conn = get_connection()
    conn.execute("SELECT 1")
    return {
        "status": "ok",
        "database": "duckdb",
    }
