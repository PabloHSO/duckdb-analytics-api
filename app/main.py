from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.datasets import router as dataset_router
from app.api.routes.queries import router as query_router
from app.api.routes.analytics import router as analytics_router
from app.core.logging import setup_logging
from app.api.middlewares.request_context import request_context_middleware
from app.api.routes.metrics import router as metrics_router
from app.api.routes.root import root_routes as root_router
from fastapi.staticfiles import StaticFiles

def create_app() -> FastAPI:

    app = FastAPI(
        title="DuckDB Analytics API",
        description="API analítica usando FastAPI + DuckDB + Docker",
        version="1.0.0",
    )

    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    # Rotas
    app.include_router(health_router)
    app.include_router(dataset_router)
    app.include_router(query_router)
    app.include_router(analytics_router)
    app.include_router(metrics_router)
    app.include_router(root_router)

    # Configuração do logging
    setup_logging()

    # Middlewares
    app.middleware("http")(request_context_middleware)

    return app


app = create_app()

# Para rodar com: uvicorn app.main:app --reload
# Comanda para rodar com docker: docker-compose up --build