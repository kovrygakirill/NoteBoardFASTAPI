from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

from app.models import note as models
from app.schemas import note as schemas
from app.service import note as service
from app.db import get_db


router = APIRouter()


@router.post(
    "/",
    response_model=schemas.NoteBase,
    status_code=201
)
def create_note(
        note: schemas.NoteCreate,
        db: Session = Depends(get_db)
) -> models.Note:
    return service.create_note(
        note_data=note,
        db=db,
    )


@router.get(
    "/{note_id}",
    response_model=schemas.Note,
    status_code=200
)
def get_board(
        note_id: UUID,
        db: Session = Depends(get_db)
) -> models.Note:
    return service.get_note_by_id(
        note_id=note_id,
        db=db
    )


@router.get(
    "/",
    response_model=list[schemas.Note],
    status_code=200
)
def get_boards(
        db: Session = Depends(get_db)
) -> list[models.Note]:
    return service.get_notes(db=db)


@router.put(
    "/{note_id}",
    response_model=schemas.Note,
    status_code=200
)
def update_board(
        note_id: UUID,
        note: schemas.NoteUpdate,
        db: Session = Depends(get_db)
) -> models.Note:
    return service.update_note(
        note_id=note_id,
        note_data=note,
        db=db,
    )


@router.delete(
    "/{note_id}",
    status_code=204
)
def delete_board(
        note_id: UUID,
        db: Session = Depends(get_db)
):
    return service.delete_note(
        note_id=note_id,
        db=db,
    )
