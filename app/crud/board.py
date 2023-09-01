from uuid import UUID
from sqlalchemy import (
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.schemas import board as schemas_board
from app.models.board import Board
from app.models.note import Note
from .base import BaseCRUD


class BoardCRUD(BaseCRUD):
    def __init__(
            self,
            db: AsyncSession
    ):
        super().__init__(db=db)

    async def create_board(
            self,
            data: schemas_board.BoardCreate,
    ) -> Board:
        board = Board(**data.dict())
        return await self.create_obj(obj=board)

    async def get_board(
            self,
            board_id: UUID,
    ) -> Board | None:
        query = select(Board).options(
            joinedload(Board.notes)
        ).where(Board.id == board_id)
        return await self.get_obj(query=query)

    async def get_boards(
            self,
            skip: int = 0,
            limit: int = 100,
    ) -> list[Board]:
        query = select(Board).options(
            joinedload(Board.notes)
        ).limit(limit).offset(skip)
        return await self.get_objs(query=query)

    async def update_board(
            self,
            board: Board,
            update_data: schemas_board.BoardUpdate,
    ) -> Board:
        query = update(Board).where(
            Board.id == board.id
        ).values(
            **update_data.dict(exclude_unset=True)
        )
        await self.update_obj(query=query)
        return board

    async def delete_board(
            self,
            board: Board,
    ) -> bool:
        return await self.delete_obj(obj=board)

    async def delete_note_from_board(
            self,
            board: Board,
            note: Note
    ) -> bool:
        board.notes.remove(note)
        await self.db.commit()
        return True

    async def add_note_to_board(
            self,
            board: Board,
            note: Note
    ) -> Board:
        board.notes.append(note)
        await self.db.commit()
        await self.db.refresh(board)
        return board
