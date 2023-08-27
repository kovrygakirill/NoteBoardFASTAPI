from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class BoardBase(BaseModel):
    id: UUID


class BoardCreate(BaseModel):
    name: str


class Board(BoardBase):
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
