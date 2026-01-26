import logging
import sys
import json
from datetime import datetime

# logging configuration (logging.Formatter - custom JSON formatter)
class JsonFormatter(logging.Formatter):
    # Format log records as JSON
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(), # UTC timestamp
            "level": record.levelname, # Log level
            "message": record.getMessage(), # Log message
            "module": record.module, # Module name
        }
        return json.dumps(log_record)

# Configuração do logger
def setup_logging():
    # Configura o logger raiz para usar o JsonFormatter
    handler = logging.StreamHandler(sys.stdout)
    # Define o formato do log como JSON
    handler.setFormatter(JsonFormatter())
    # Configura o logger raiz
    root = logging.getLogger()
    # Define o nível de log
    root.setLevel(logging.INFO)
    # Adiciona o handler configurado
    root.handlers = [handler]
