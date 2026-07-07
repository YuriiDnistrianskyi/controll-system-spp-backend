from sqlalchemy.ext.asyncio import AsyncSession

from app.service.base_service import BaseService
from app.database.models.connected_device import ConnectedDevice
from app.schemas.connected_device_schemas import CreateConnectedDeviceSchema, UpdateConnectedDeviceSchema

class ConnectedDeviceService(BaseService[ConnectedDevice]):

    async def create(self, schema: CreateConnectedDeviceSchema, session: AsyncSession) -> ConnectedDevice:
        obj = ConnectedDevice(
            name=schema.name,
            mac_address=schema.mac_address,
            gateway_device_id=schema.gateway_device_id,
            priority=schema.priority,
        )

        await self.repository.add(obj, session)
        return obj

    async def update(self, id: int, schema: UpdateConnectedDeviceSchema, session: AsyncSession) -> ConnectedDevice:
        obj = await self.repository.get_by_id(id, session)
        data_dict = schema.model_dump(exclude_unset=True)

        if 'name' in data_dict:
            obj.name = data_dict.get('name')

        if 'mac_address' in data_dict:
            obj.mac_address = data_dict.get('mac_address')

        if 'gateway_device_id' in data_dict:
            obj.gateway_device_id = data_dict.get('gateway_device_id')

        if 'priority' in data_dict:
            obj.priority = data_dict.get('priority')

        return obj