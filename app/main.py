from fastapi import FastAPI
from app.api.routes.health import router as health_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="DuckDB Analytics API",
        description="API analítica usando FastAPI + DuckDB + Docker",
        version="1.0.0",
    )

    # Rotas
    app.include_router(health_router, prefix="/health", tags=["Health"])

    return app


app = create_app()