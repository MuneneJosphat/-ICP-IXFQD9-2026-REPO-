
from datetime import datetime
from pydantic import BaseModel


class MessageIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    label: str
    is_spam: bool


class PredictionLog(BaseModel):
    id: int
    text: str
    label: str
    is_spam: bool
    created_at: datetime

    class Config:
        orm_mode = True
