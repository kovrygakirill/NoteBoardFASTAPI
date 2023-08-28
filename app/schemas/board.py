from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

from .note import Note


class BoardBase(BaseModel):
    id: UUID


class BoardCreate(BaseModel):
    name: str


class Board(BoardBase):
    name: str
    created_at: datetime
    updated_at: datetime | None
    notes: list[Note] | None


class BoardUpdate(BaseModel):
    name: str | None = None
