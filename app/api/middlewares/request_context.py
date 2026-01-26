import time
import uuid
import logging
from fastapi import Request

from app.api.routes.metrics import REQUEST_COUNT, REQUEST_LATENCY

logger = logging.getLogger(__name__)

async def request_context_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4()) # Gera um UUID único para cada requisição
    start_time = time.time() # Marca o tempo de início da requisição

    response = await call_next(request) # Processa a requisição

    process_time = time.time() - start_time # Calcula o tempo de processamento

    endpoint = request.url.path # Obtém o endpoint da requisição
    method = request.method # Obtém o método HTTP da requisição
    status = response.status_code # Obtém o status da resposta

    # 🔹 Prometheus metrics
    REQUEST_COUNT.labels(
        method=method,
        endpoint=endpoint,
        status=status
    ).inc()

    # 🔹 Prometheus metrics (Latência)
    REQUEST_LATENCY.labels(
        endpoint=endpoint
    ).observe(process_time)

    # Headers
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time"] = str(round(process_time, 4))

    # Log estruturado
    logger.info(
        "request completed",
        extra={
            "request_id": request_id,
            "method": method,
            "path": endpoint,
            "status_code": status,
            "process_time": process_time,
        },
    )

    return response
