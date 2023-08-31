from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import note as schemas
from app.service import note as service
from app.db import get_db as session

router = APIRouter()


@router.post(
    "/",
    response_model=schemas.NoteBase,
    status_code=201
)
async def create_note(
        note: schemas.NoteCreate,
        db: AsyncSession = Depends(session)
):
    return await service.create_note(
        note_data=note,
        db=db,
    )


@router.get(
    "/{note_id}",
    response_model=schemas.Note,
    status_code=200
)
async def get_note(
        note_id: UUID,
        db: AsyncSession = Depends(session)
):
    return await service.get_note_by_id(
        note_id=note_id,
        db=db
    )


@router.get(
    "/",
    response_model=list[schemas.Note],
    status_code=200
)
async def get_notes(
        db: AsyncSession = Depends(session)
):
    return await service.get_notes(db=db)


@router.put(
    "/{note_id}",
    response_model=schemas.Note,
    status_code=200
)
async def update_note(
        note_id: UUID,
        note: schemas.NoteUpdate,
        db: AsyncSession = Depends(session)
):
    return await service.update_note(
        note_id=note_id,
        note_data=note,
        db=db,
    )


@router.delete(
    "/{note_id}",
    status_code=204
)
async def delete_note(
        note_id: UUID,
        db: AsyncSession = Depends(session)
):
    return await service.delete_note(
        note_id=note_id,
        db=db,
    )


@router.post(
    "/{note_id}/views",
    status_code=204
)
async def increment_note_views(
        note_id: UUID,
        db: AsyncSession = Depends(session)
):
    return await service.increment_note_views(
        note_id=note_id,
        db=db,
    )
