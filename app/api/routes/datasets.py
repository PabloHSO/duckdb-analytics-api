from fastapi import APIRouter, HTTPException
from app.services.dataset_service import DatasetService
from app.schemas.dataset import (
    DatasetIngestResponse,
    DatasetLoadRequest,
    DatasetLoadResponse,
)

router = APIRouter(prefix="/datasets", tags=["Datasets"])


@router.post("/ingest", response_model=DatasetIngestResponse)
def ingest_dataset():
    '''
    Ingere o conjunto de dados de vendas de exemplo no banco de dados DuckDB.
    Esta função chama o serviço de ingestão de dados que lê um arquivo CSV
    '''
    return DatasetService.ingest_sales()


@router.post("/load", response_model=DatasetLoadResponse)
def load_dataset(payload: DatasetLoadRequest):
    '''
    Carrega um dataset CSV como uma tabela no banco de dados DuckDB.
    Recebe o nome da tabela e o caminho do arquivo CSV na requisição.
    '''
    try:
        rows = DatasetService.load_csv_as_table(
            table_name=payload.name,
            file_path=payload.path
        )

        return DatasetLoadResponse(
            message="Dataset carregado com sucesso",
            table=payload.name,
            rows_loaded=rows
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
