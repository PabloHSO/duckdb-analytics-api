from pydantic import BaseModel

class DatasetIngestResponse(BaseModel):
    status: str
