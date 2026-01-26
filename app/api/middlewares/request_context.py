import time
import uuid
import logging
from fastapi import Request


logger = logging.getLogger(__name__)

# Middleware para adicionar contexto de requisição
async def request_context_middleware(request: Request, call_next):
    # Gerar um ID único para a requisição
    request_id = str(uuid.uuid4())
    # startar o timer
    start_time = time.time()

    # Processar a requisição
    response = await call_next(request)

    # Calcular o tempo de processamento
    process_time = time.time() - start_time

    # Adicionar headers à resposta
    response.headers["X-Request-ID"] = request_id # ID único da requisição
    response.headers["X-Process-Time"] = str(round(process_time, 4)) #  Tempo de processamento
    
    # Logar a requisição concluída
    logger.info(
        "request completed",
        extra={
            "request_id": request_id, # ID único da requisição
            "method": request.method, # Método HTTP
            "path": request.url.path, # Caminho da URL
            "status_code": response.status_code, # Código de status da resposta
            "process_time": process_time, # Tempo de processamento
        },
    )

    return response
