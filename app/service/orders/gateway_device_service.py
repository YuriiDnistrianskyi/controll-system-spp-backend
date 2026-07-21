from alembic.command import branches
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict
import secrets

from app.service.base_service import BaseService
from app.database.models.gateway_device import GatewayDevice
from app.repository.relational.gateway_device_repository import GatewayDeviceRepository
from app.schemas.gateway_device_schemas import CreateGatewayDeviceSchema, UpdateGatewayDeviceSchema, AuthGatewayDeviceSchema, InitGatewayDeviceSchema
from app.core.serurity import create_hash, verify_hash, create_lookup
from app.ws import ws_manager


class GatewayDeviceService(BaseService[GatewayDevice]):
    def __init__(self, repository: GatewayDeviceRepository) -> None:
        self.repository = repository

    async def create(self, schema: CreateGatewayDeviceSchema, session: AsyncSession) -> Dict[str, Any]:
        token = await self.__create_token(session)
        obj = GatewayDevice(
            name=schema.name,
            token_hash=create_hash(token),
            token_lookup=create_lookup(token),
            system_id=schema.system_id,
        )

        await self.repository.add(obj, session)
        return {
            'obj': obj,
            'token': token
        }

    async def __create_token(self, session: AsyncSession) -> str:
        while True:
            token: str = secrets.token_hex(32)

            exist = await self.repository.get_by_token_lookup(create_lookup(token), session)

            if exist is None:
                return token


    async def update(self, id: int, schema: UpdateGatewayDeviceSchema, session: AsyncSession) -> GatewayDevice:
        obj = await self.repository.get_by_id(id, session)
        data_dict = schema.model_dump(exclude_unset=True)

        if 'name' in data_dict:
            obj.name = data_dict['name']

        if 'mac_address' in data_dict:
            obj.mac_address = data_dict['mac_address']

        if 'system_id' in data_dict:
            obj.system_id = data_dict['system_id']

        return obj

    # async def update_token(self):
    #     pass

    async def authenticate(self, schema: AuthGatewayDeviceSchema, session: AsyncSession) -> int:
        data = schema.model_dump(exclude_unset=True)

        gateway = await self.repository.get_by_id(data['id'], session)
        is_auth: bool = verify_hash(str(gateway.token_hash), data['token'])
        if not is_auth:
            raise HTTPException(status_code=401, detail='Invalid token')
        return data['id']

    async def initialize(self, schema: InitGatewayDeviceSchema, session: AsyncSession) -> int:
        data = schema.model_dump(exclude_unset=True)

        gateway: GatewayDevice = await self.repository.get_by_token_lookup(create_lookup(data['token']), session)
        if gateway is None:
            raise HTTPException(status_code=404, detail='Gateway not found')

        gateway.mac_address = data['mac_address']
        await session.commit()

        await ws_manager.switch(data['mac_address'], gateway.id)

        msg = {
            'type': 'success_auth',
            'gateway_id': gateway.id
        }

        await ws_manager.send(gateway.id, msg)

        return int(gateway.id)
