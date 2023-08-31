from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import board as schemas_board
from app.schemas import note as schemas_note
from app.service import board as service
from app.db import get_db as session

router = APIRouter()


@router.post(
    "/",
    response_model=schemas_board.BoardBase,
    status_code=201
)
async def create_board(
        board: schemas_board.BoardCreate,
        db: AsyncSession = Depends(session)
):
    return await service.create_board(
        board_data=board,
        db=db,
    )


@router.get(
    "/{board_id}",
    response_model=schemas_board.Board,
    status_code=200
)
async def get_board(
        board_id: UUID,
        db: AsyncSession = Depends(session)
):
    return await service.get_board_by_id(
        board_id=board_id,
        db=db
    )


@router.get(
    "/",
    response_model=list[schemas_board.Board],
    status_code=200
)
async def get_boards(
        db: AsyncSession = Depends(session)
):
    return await service.get_boards(db=db)


@router.put(
    "/{board_id}",
    response_model=schemas_board.Board,
    status_code=200
)
async def update_board(
        board_id: UUID,
        board: schemas_board.BoardUpdate,
        db: AsyncSession = Depends(session)
):
    return await service.update_board(
        board_id=board_id,
        board_data=board,
        db=db,
    )


@router.delete(
    "/{board_id}",
    status_code=204
)
async def delete_board(
        board_id: UUID,
        db: AsyncSession = Depends(session)
):
    return await service.delete_board(
        board_id=board_id,
        db=db,
    )


@router.post(
    "/{board_id}/notes",
    response_model=schemas_board.Board,
    status_code=200
)
async def add_note_to_board(
        board_id: UUID,
        note: schemas_note.NoteAdd,
        db: AsyncSession = Depends(session)
):
    return await service.add_note_to_board(
        board_id=board_id,
        note=note,
        db=db
    )


@router.delete(
    "/{board_id}/notes/{note_id}",
    status_code=204
)
async def delete_note_from_board(
        board_id: UUID,
        note_id: UUID,
        db: AsyncSession = Depends(session)
):
    return await service.delete_note_from_board(
        board_id=board_id,
        note_id=note_id,
        db=db
    )
