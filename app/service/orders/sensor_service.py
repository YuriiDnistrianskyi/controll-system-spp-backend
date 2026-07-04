from sqlalchemy.ext.asyncio import AsyncSession

from app.service.base_service import BaseService
from app.database.models.sensor import Sensor
from app.schemas.sensor_schemas import CreateSensorSchema, UpdateSensorSchema


class SensorService(BaseService[Sensor]):
    pass

    async def create(self, schema: CreateSensorSchema, session: AsyncSession) -> Sensor:
        obj = Sensor(
            name=schema.name,
            mac_address=schema.mac_address,
            type_id=schema.type_id,
            system_id=schema.system_id,
        )

        await self.repository.add(obj, session)
        return obj

    async def update(self, id: int, schema: UpdateSensorSchema, session: AsyncSession) -> Sensor:
        obj = await self.repository.get_by_id(id, session)
        data_dict = schema.model_dump(exclude_unset=True)

        if 'name' in data_dict:
            obj.name = data_dict['name']

        if 'mac_address' in data_dict:
            obj.mac_address = data_dict['mac_address']

        if 'type_id' in data_dict:
            obj.type_id = data_dict['type_id']

        if 'system_id' in data_dict:
            obj.system_id = data_dict['system_id']

        return obj
