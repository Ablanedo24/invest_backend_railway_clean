
from pydantic import BaseModel

class InversionIn(BaseModel):
    ticker: str
    monto: float
