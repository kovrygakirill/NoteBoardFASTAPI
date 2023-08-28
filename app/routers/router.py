from fastapi import APIRouter

from app.routers import (
    note,
    board,
)

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

router.include_router(
    note.router,
    prefix='/note'
)
router.include_router(
    board.router,
    prefix='/board'
)


