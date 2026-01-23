import duckdb # Importa a biblioteca duckdb para manipulação do banco de dados DuckDB
from pathlib import Path # Importa Path para manipulação de caminhos de arquivos

# Define o caminho do arquivo do banco de dados DuckDB
DB_PATH = Path("data/analytics.duckdb")

# Função para obter uma conexão com o banco de dados DuckDB
def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return duckdb.connect(str(DB_PATH))