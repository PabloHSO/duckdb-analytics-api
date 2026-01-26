FROM python:3.11-slim

# Evita arquivos .pyc e buffer no stdout (útil para logs)
# stdout -> terminal em tempo real ao invés de armazenar em buffer

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código da aplicação
COPY app ./app
COPY data ./data

# Expor porta da API
EXPOSE 8000

# Comando de inicialização
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
