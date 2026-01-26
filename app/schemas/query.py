from pydantic import BaseModel, Field
from typing import Optional

class TopUserResponse(BaseModel):
    user_id: int
    total_spent: float

class QueryRequest(BaseModel):
    metric: str = Field(..., example="total_sales")
    start_date: Optional[str] = Field(None, example="2025-01-01")
    end_date: Optional[str] = Field(None, example="2025-12-31")

class QueryResponse(BaseModel):
    metric: str
    result: float