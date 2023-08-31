from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select
from sqlalchemy.sql.dml import Update

from app.db import Base


class BaseCRUD:
    def __init__(
            self,
            db: AsyncSession,
    ):
        self.db = db

    async def create_obj(
            self,
            obj: Base,
    ) -> Base:
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def get_obj(
            self,
            query: Select,
    ) -> Base | None:
        result = await self.db.execute(query)
        return result.scalars().first()

    async def get_objs(
            self,
            query: Select,
    ) -> list[Base]:
        result = await self.db.execute(query)
        return result.unique().scalars().all()

    async def update_obj(
            self,
            query: Update,
    ) -> Base:
        result = await self.db.execute(query)
        await self.db.commit()
        return result.scalars().first()

    async def delete_obj(
            self,
            obj: Base,
    ) -> bool:
        await self.db.delete(obj)
        await self.db.commit()
        return True
