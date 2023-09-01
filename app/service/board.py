from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.board import Board
from app.models.note import Note
from app.schemas import board as schemas_board
from app.schemas import note as schemas_note
from app.crud.board import BoardCRUD
from app.exceptions import (
    BoardNotExist,
    NoteNotBelongBoard,
)
from app.service import note as service_note


async def create_board(
        board_data: schemas_board.BoardCreate,
        db: AsyncSession,
) -> Board:
    return await BoardCRUD(db=db).create_board(
        data=board_data,
    )


async def get_board_by_id(
        board_id: UUID,
        db: AsyncSession,
) -> Board:
    board = await BoardCRUD(db=db).get_board(
        board_id=board_id
    )

    if not board:
        raise BoardNotExist

    return board


async def get_boards(
        db: AsyncSession,
) -> list[Board]:
    return await BoardCRUD(db=db).get_boards()


async def update_board(
        board_id: UUID,
        board_data: schemas_board.BoardUpdate,
        db: AsyncSession,
) -> Board:
    board = await get_board_by_id(
        board_id=board_id,
        db=db,
    )

    return await BoardCRUD(db=db).update_board(
        board=board,
        update_data=board_data
    )


async def delete_board(
        board_id: UUID,
        db: AsyncSession,
) -> bool:
    board = await get_board_by_id(
        board_id=board_id,
        db=db,
    )

    return await BoardCRUD(db=db).delete_board(
        board=board,
    )


async def add_note_to_board(
        board_id: UUID,
        note: schemas_note.NoteAdd,
        db: AsyncSession,
) -> Board:
    board = await get_board_by_id(
        board_id=board_id,
        db=db,
    )
    note_obj = Note(**note.dict(), board_id=board_id)

    return await BoardCRUD(db=db).add_note_to_board(
        board=board,
        note=note_obj
    )


async def delete_note_from_board(
        board_id: UUID,
        note_id: UUID,
        db: AsyncSession,
) -> bool:
    board = await get_board_by_id(
        board_id=board_id,
        db=db,
    )
    note = await service_note.get_note_by_id(
        note_id=note_id,
        db=db,
    )

    if note not in board.notes:
        raise NoteNotBelongBoard

    return await BoardCRUD(db=db).delete_note_from_board(
        board=board,
        note=note
    )
