from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.relational import DeviceTypeRepository
from app.service.base.base_service import BaseService
from app.repository.relational.base_repository import BaseRepository
from app.database.models.sensor import Sensor
from app.schemas.sensor_schemas import CreateSensorSchema, UpdateSensorSchema


class SensorService(BaseService[Sensor]):

    def __init__(self, repository: BaseRepository[Sensor], device_type_repository: DeviceTypeRepository):
        super().__init__(repository)
        self.device_type_repository = device_type_repository

    async def create(self, schema: CreateSensorSchema, session: AsyncSession) -> Sensor:
        if schema.type == 'front_battery':
            device_type_id = await self.device_type_repository.get_front_battery_type_id(session)
        elif schema.type == 'back_battery':
            device_type_id = await self.device_type_repository.get_back_battery_type_id(session)
        else:
            raise #TODO

        obj = Sensor(
            name=schema.name,
            mac_address=schema.mac_address,
            type_id=device_type_id,
            gateway_device_id=schema.gateway_device_id,
        )

        await self.repository.add(obj, session)
        return obj

    async def update(self, id: int, schema: UpdateSensorSchema, session: AsyncSession) -> Sensor:
        obj = await self.repository.get_by_id(id, session)
        data_dict = schema.model_dump(exclude_unset=True)

        if 'name' in data_dict:
            obj.name = data_dict['name']

        if 'mac_address' in data_dict: #
            obj.mac_address = data_dict['mac_address']

        if 'type_id' in data_dict: #
            obj.type_id = data_dict['type_id']

        if 'gateway_device_id' in data_dict:
            obj.gateway_device_id = data_dict['gateway_device_id']

        return obj
