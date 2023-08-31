from uuid import UUID
from sqlalchemy import (
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import note as schemas
from app.models.note import Note
from .base import BaseCRUD


class NoteCRUD(BaseCRUD):
    def __init__(
            self,
            db: AsyncSession
    ):
        super().__init__(db=db)

    async def create_note(
            self,
            data: schemas.NoteCreate,
    ) -> Note:
        note = Note(**data.dict())
        return await self.create_obj(obj=note)

    async def get_note(
            self,
            note_id: UUID,
    ) -> Note | None:
        query = select(Note).where(
            Note.id == note_id
        )
        return await self.get_obj(query=query)

    async def get_notes(
            self,
            skip: int = 0,
            limit: int = 100,
    ) -> list[Note]:
        query = select(Note).limit(limit).offset(skip)
        return await self.get_objs(query=query)

    async def update_note(
            self,
            note_id: UUID,
            update_data: schemas.NoteUpdate,
    ) -> Note:
        query = update(Note).where(
            Note.id == note_id
        ).values(
            **update_data.dict(exclude_unset=True)
        ).returning(Note)
        return await self.update_obj(query=query)

    async def delete_note(
            self,
            note: Note,
    ) -> bool:
        return await self.delete_obj(obj=note)
