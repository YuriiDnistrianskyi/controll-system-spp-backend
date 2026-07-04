from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.base_repository import BaseRepository
from app.database.models.device_type import DeviceType


class DeviceTypeRepository:
    async def get_back_battery_type_id(self, session: AsyncSession) -> int:
        stmt = select(DeviceType).where(DeviceType.type == 'back_battery')
        result = await session.execute(stmt)
        back_battery_type_id = result.scalar().first()
        return back_battery_type_id

    async def get_front_battery_type_id(self, session: AsyncSession) -> int:
        stmt = select(DeviceType).where(DeviceType.type == 'front_battery')
        result = await session.execute(stmt)
        front_battery_type_id = result.scalar().first()
        return front_battery_type_id
