from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.role_type import RoleType


class RoleTypeRepository:
    async def get_admin_type_id(self, session: AsyncSession) -> int:
        stmt = select(RoleType).where(RoleType.type == 'admin')
        result = await session.execute(stmt)
        admin_type_id = result.scalar().first()
        return admin_type_id

    async def get_observer_type_id(self, session: AsyncSession) -> int:
        stmt = select(RoleType).where(RoleType.type == 'observer')
        result = await session.execute(stmt)
        observer_type = result.scalar().first()
        return observer_type
