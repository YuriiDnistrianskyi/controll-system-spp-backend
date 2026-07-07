from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.user_to_system import UserToSystem


class UserToSystemRepository:
    async def get_by_ids(self, user_id: int, system_id, session: AsyncSession) -> UserToSystem:
        stmt = select(UserToSystem).where(UserToSystem.id == user_id and UserToSystem.system_id == system_id)
        result = await session.execute(stmt)
        return result.scalars().first()


