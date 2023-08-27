from fastapi import APIRouter

from app.routers import (
    note,
    board,
)

router = APIRouter()

router.include_router(
    note.router,
    prefix='/note'
)
router.include_router(
    board.router,
    prefix='/board'
)


