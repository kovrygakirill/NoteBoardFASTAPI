from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from app.models import board as models
from app.schemas import board as schemas
from app import crud
from app.db import get_db
from app.exceptions import BoardNotExist


def create_board(
        board_data: schemas.BoardCreate,
        db: Session = Depends(get_db)
) -> models.Board:
    return crud.create_obj(
        obj_data=board_data,
        type_obj=models.Board,
        db=db,
    )


def get_board_by_id(
        board_id: UUID,
        db: Session = Depends(get_db)
) -> models.Board:
    board = crud.get_obj(
        type_obj=models.Board,
        obj_id=board_id,
        db=db,
    )

    if not board:
        raise BoardNotExist

    return board


def get_boards(
        db: Session = Depends(get_db)
) -> list[models.Board]:
    return crud.get_objs(
        type_obj=models.Board,
        db=db,
    )


def update_board(
        board_id: UUID,
        board_data: schemas.BoardUpdate,
        db: Session,
) -> models.Board:
    board = get_board_by_id(
        board_id=board_id,
        db=db,
    )

    return crud.update_obj(
        type_obj=models.Board,
        obj_id=board_id,
        obj_data=board_data,
        db=db,
    )


def delete_board(
        board_id: UUID,
        db: Session = Depends(get_db)
) -> bool:
    board = get_board_by_id(
        board_id=board_id,
        db=db,
    )

    return crud.remove_obj(
        obj=board,
        db=db,
    )
