FROM python:3.12-slim

# Definir variáveis de ambiente para evitar a criação de arquivos .pyc e para saída não bufferizada
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalar dependências do sistema
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY app ./app
COPY data ./data

# Criar um usuário não-root para rodar a aplicação
RUN addgroup --system app && adduser --system --group app
USER app

# Expor a porta que a aplicação irá rodar
EXPOSE 8000

# Para iniciar a aplicação FastAPI com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
