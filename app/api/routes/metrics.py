from fastapi import APIRouter
# Importações para métricas Prometheus
from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response

router = APIRouter(tags=["Metrics"])

# Contadores e histogramas para métricas Prometheus
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)

# Latência das requisições
REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency",
    ["endpoint"],
)

@router.get("/metrics")
def metrics():
    '''
    Endpoint para expor métricas Prometheus
    '''
    return Response(generate_latest(), media_type="text/plain")
