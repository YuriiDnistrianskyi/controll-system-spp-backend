from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict

from app.service.base_service import BaseService
from app.database.models.gateway_device import GatewayDevice
from app.schemas.gateway_device_schemas import CreateGatewayDeviceSchema, UpdateGatewayDeviceSchema
from app.core.serurity import create_hash


class GatewayDeviceService(BaseService[GatewayDevice]):
    async def create(self, schema: CreateGatewayDeviceSchema, session: AsyncSession) -> Dict[str, Any]:
        token = 'token' #TODO
        obj = GatewayDevice(
            name=schema.name,
            token_hash=create_hash(token),
            mac_address=schema.mac_address,
            system_id=schema.system_id,
        )

        await self.repository.add(obj, session)
        return {
            'obj': obj,
            'token': token
        }


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
