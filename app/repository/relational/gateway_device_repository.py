from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.repository.relational.base_repository import BaseRepository
from app.database.models.gateway_device import GatewayDevice


class GatewayDeviceRepository(BaseRepository[GatewayDevice]):
    async def get_by_token_hash(self, token_hash: str, session: AsyncSession) -> GatewayDevice:
        stmt = select(GatewayDevice).where(GatewayDevice.token_hash == token_hash)
        obj = await session.execute(stmt)
        result = obj.scalars().one()

        return result

