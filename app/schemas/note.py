from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

from models.board import Board


class NoteBase(BaseModel):
    id: UUID


class NoteCreate(BaseModel):
    text: str
    board_id: UUID


class Note(NoteBase):
    text: str
    created_at: datetime
    updated_at: datetime
    views: int
    board: Board

    class Config:
        orm_mode = True
