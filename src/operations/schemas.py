from datetime import datetime
from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    Instrument_type: str
    date: datetime
    type: str
