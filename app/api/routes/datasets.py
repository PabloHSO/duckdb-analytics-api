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
    return DatasetService.ingest_sales()


@router.post("/load", response_model=DatasetLoadResponse)
def load_dataset(payload: DatasetLoadRequest):
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
