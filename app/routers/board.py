from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

from app.models import board as models
from app.schemas import board as schemas
from app.service import board as service
from app.db import get_db


router = APIRouter()


@router.post(
    "/",
    response_model=schemas.BoardBase,
    status_code=201
)
def create_board(
        board: schemas.BoardCreate,
        db: Session = Depends(get_db)
) -> models.Board:
    return service.create_board(
        board_data=board,
        db=db,
    )


@router.get(
    "/{board_id}",
    response_model=schemas.Board,
    status_code=200
)
def get_board(
        board_id: UUID,
        db: Session = Depends(get_db)
) -> models.Board:
    return service.get_board_by_id(
        board_id=board_id,
        db=db
    )


@router.get(
    "/",
    response_model=list[schemas.Board],
    status_code=200
)
def get_boards(
        db: Session = Depends(get_db)
) -> list[models.Board]:
    return service.get_boards(db=db)


@router.put(
    "/{board_id}",
    response_model=schemas.Board,
    status_code=200
)
def update_board(
        board_id: UUID,
        board: schemas.BoardUpdate,
        db: Session = Depends(get_db)
) -> models.Board:
    return service.update_board(
        board_id=board_id,
        board_data=board,
        db=db,
    )


@router.delete(
    "/{board_id}",
    status_code=204
)
def delete_board(
        board_id: UUID,
        db: Session = Depends(get_db)
):
    return service.delete_board(
        board_id=board_id,
        db=db,
    )
