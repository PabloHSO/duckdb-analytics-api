from fastapi import APIRouter
from app.services.dataset_service import ingest_sales
from app.schemas.dataset import DatasetIngestResponse

router = APIRouter(prefix="/datasets", tags=["Datasets"])

@router.post("/ingest", response_model=DatasetIngestResponse)
def ingest_dataset():
    return ingest_sales()
