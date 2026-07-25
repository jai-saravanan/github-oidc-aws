from pydantic import BaseModel
from datetime import datetime


class Customer(BaseModel):
    id: int = None
    name: str
    phone: str = None
    created_at: datetime = None

    class Config:
        from_attributes = True


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
