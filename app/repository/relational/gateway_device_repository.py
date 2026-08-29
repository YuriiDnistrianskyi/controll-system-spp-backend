from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.repository.relational.base_repository import BaseRepository
from app.database.models.gateway_device import GatewayDevice


class GatewayDeviceRepository(BaseRepository[GatewayDevice]):
    _model = GatewayDevice

    async def get_by_activate_code(self, activate_code_hash: str, session: AsyncSession) -> GatewayDevice:
        stmt = select(GatewayDevice).where(self._model.activate_code_hash == activate_code_hash)
        obj = await session.execute(stmt)
        result = obj.scalars().first()

        return result


    async def get_by_token_lookup(self, token_lookup: str, session: AsyncSession) -> GatewayDevice:
        stmt = select(GatewayDevice).where(self._model.token_lookup == token_lookup)
        obj = await session.execute(stmt)
        result = obj.scalars().one_or_none()

        return result
