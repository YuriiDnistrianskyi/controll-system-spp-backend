from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.device_type import DeviceType


class DeviceTypeRepository:
    async def get_back_battery_type_id(self, session: AsyncSession) -> int:
        stmt = select(DeviceType).where(DeviceType.code == 'BACK_SENSOR')
        result = await session.execute(stmt)
        back_battery_type_id = result.scalar().first()
        return back_battery_type_id

    async def get_front_battery_type_id(self, session: AsyncSession) -> int:
        stmt = select(DeviceType).where(DeviceType.code == 'FRONT_SENSOR')
        result = await session.execute(stmt)
        front_battery_type_id = result.scalar().first()
        return front_battery_type_id
