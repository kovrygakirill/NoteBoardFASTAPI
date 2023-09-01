from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.note import Note
from app.schemas import note as schemas
from app.service import board as service_board
from app.crud.note import NoteCRUD
from app.exceptions import NoteNotExist


async def create_note(
        note_data: schemas.NoteCreate,
        db: AsyncSession,
) -> Note:
    board = await service_board.get_board_by_id(
        board_id=note_data.board_id,
        db=db
    )
    return await NoteCRUD(db=db).create_note(
        data=note_data,
    )


async def get_note_by_id(
        note_id: UUID,
        db: AsyncSession,
) -> Note:
    note = await NoteCRUD(db=db).get_note(
        note_id=note_id,
    )

    if not note:
        raise NoteNotExist

    return note


async def get_notes(
        db: AsyncSession
) -> list[Note]:
    return await NoteCRUD(db=db).get_notes()


async def update_note(
        note_id: UUID,
        note_data: schemas.NoteUpdate,
        db: AsyncSession,
) -> Note:
    note = await get_note_by_id(
        note_id=note_id,
        db=db,
    )

    if board_id := note_data.board_id:
        board = await service_board.get_board_by_id(
            board_id=board_id,
            db=db,
        )

    return await NoteCRUD(db=db).update_note(
        note=note,
        update_data=note_data,
    )


async def delete_note(
        note_id: UUID,
        db: AsyncSession,
) -> bool:
    note = await get_note_by_id(
        note_id=note_id,
        db=db,
    )

    return await NoteCRUD(db=db).delete_note(
        note=note,
    )


async def increment_note_views(
        note_id: UUID,
        db: AsyncSession,
) -> True:
    note = await get_note_by_id(
        note_id=note_id,
        db=db,
    )
    note.views += 1

    await db.commit()

    return True
