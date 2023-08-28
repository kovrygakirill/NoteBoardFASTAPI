from uuid import UUID
from sqlalchemy.orm import Session

from app.db import Base
from app.schemas import board as schemas


def create_obj(
        type_obj: Base,
        obj_data: schemas.BaseModel,
        db: Session,
) -> Base:
    obj = type_obj(**obj_data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_obj(
        type_obj: Base,
        obj_id: UUID,
        db: Session,
) -> Base | None:
    return db.query(type_obj).filter(
        type_obj.id == obj_id
    ).first()


def get_objs(
        type_obj: Base,
        db: Session,
        skip: int = 0,
        limit: int = 100,
) -> list[Base]:
    return db.query(type_obj).offset(skip).limit(limit).all()


def update_obj(
        type_obj: Base,
        obj_id: UUID,
        obj_data: schemas.BaseModel,
        db: Session
) -> Base:
    obj_query = db.query(type_obj).filter(
        type_obj.id == obj_id
    )
    updated_obj = obj_query.first()

    obj_query.update(
        obj_data.dict(exclude_unset=True),
        synchronize_session=False
    )
    db.commit()

    return updated_obj


def remove_obj(
        obj: Base,
        db: Session,
) -> bool:
    db.delete(obj)
    db.commit()
    return True
