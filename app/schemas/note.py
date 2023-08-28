from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class NoteBase(BaseModel):
    id: UUID


class NoteCreate(BaseModel):
    text: str
    board_id: UUID


class Note(NoteBase):
    text: str
    created_at: datetime
    updated_at: datetime | None
    views: int


class NoteUpdate(BaseModel):
    text: str | None = None
