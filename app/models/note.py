import uuid

from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    DateTime,
    Integer,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db import Base


class Note(Base):
    __tablename__ = 'notes'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4
    )
    text = Column(
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
    views = Column(
        Integer,
        default=0
    )

    board_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "boards.id",
            ondelete="CASCADE",
        ),
    )
    board = relationship(
        "Board",
        back_populates="notes"
    )
