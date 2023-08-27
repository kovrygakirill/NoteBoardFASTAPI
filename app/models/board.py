import uuid

from sqlalchemy import (
    Column,
    String,
    DateTime,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db import Base


class Board(Base):
    __tablename__ = 'boards'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4
    )
    name = Column(
        String,
        nullable=False
    )
    created_at = Column(
        DateTime,
        default=func.now()
    )
    updated_at = Column(
        DateTime,
        onupdate=func.now()
    )

    notes = relationship(
        "Note",
        back_populates="board"
    )

