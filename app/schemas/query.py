from pydantic import BaseModel

class TopUserResponse(BaseModel):
    user_id: int
    total_spent: float
