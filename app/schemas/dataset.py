from pydantic import BaseModel, Field

# Modelo para requisição de ingestão de dataset
class DatasetIngestResponse(BaseModel):
    status: str

# Modelo para requisição de carregamento de dataset
class DatasetLoadRequest(BaseModel):
    name: str = Field(..., example="sales")
    path: str = Field(..., example="data/samples/sales.csv")

# Modelo para resposta de carregamento de dataset
class DatasetLoadResponse(BaseModel):
    message: str
    table: str
    rows_loaded: int