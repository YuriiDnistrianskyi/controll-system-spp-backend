from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.repository.relational.base_repository import BaseRepository
from app.database.models.gateway_device import GatewayDevice


class GatewayDeviceRepository(BaseRepository[GatewayDevice]):
    async def get_by_token_lookup(self, token_lookup: str, session: AsyncSession) -> GatewayDevice:
        stmt = select(GatewayDevice).where(GatewayDevice.token_lookup == token_lookup)
        obj = await session.execute(stmt)
        result = obj.scalars().one_or_none()

        return result
