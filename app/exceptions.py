from fastapi import HTTPException, status

BoardNotExist = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Could not find board",
)

NoteNotExist = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Could not find note",
)
