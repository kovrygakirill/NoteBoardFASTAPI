from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from app.models import note as models
from app.schemas import note as schemas
from app import crud
from app.service import board as service_board
from app.db import get_db
from app.exceptions import NoteNotExist


def create_note(
        note_data: schemas.NoteCreate,
        db: Session = Depends(get_db)
) -> models.Note:
    board = service_board.get_board_by_id(
        board_id=note_data.board_id,
        db=db
    )
    return crud.create_obj(
        type_obj=models.Note,
        obj_data=note_data,
        db=db,
    )


def get_note_by_id(
        note_id: UUID,
        db: Session = Depends(get_db)
) -> models.Note:
    note = crud.get_obj(
        type_obj=models.Note,
        obj_id=note_id,
        db=db,
    )

    if not note:
        raise NoteNotExist

    return note


def get_notes(
        db: Session = Depends(get_db)
) -> list[models.Note]:
    return crud.get_objs(
        type_obj=models.Note,
        db=db,
    )


def update_note(
        note_id: UUID,
        note_data: schemas.NoteUpdate,
        db: Session,
) -> models.Note:
    note = get_note_by_id(
        note_id=note_id,
        db=db,
    )
    board = service_board.get_board_by_id(
        board_id=note.board_id,
        db=db,
    )

    return crud.update_obj(
        type_obj=models.Note,
        obj_id=note_id,
        obj_data=note_data,
        db=db,
    )


def delete_note(
        note_id: UUID,
        db: Session = Depends(get_db)
) -> bool:
    note = get_note_by_id(
        note_id=note_id,
        db=db,
    )

    return crud.remove_obj(
        obj=note,
        db=db,
    )
