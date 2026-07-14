from sqlalchemy.ext.asyncio import AsyncSession

from app.service.orders.connected_device_service import ConnectedDeviceService
from app.service.orders.sensor_service import SensorService
from app.schemas.connected_device_schemas import CreateConnectedDeviceSchema
from app.schemas.sensor_schemas import CreateSensorSchema
from app.ws.handlers.i_handler import IHandler


class InitDeviceHandler(IHandler):
    def __init__(self, sensor_service: SensorService, connected_device_service: ConnectedDeviceService):
        self.sensor_service = sensor_service
        self.connected_device_service = connected_device_service

    async def handle(self, data: dict) -> None:
        session: AsyncSession = None
        gateway_id = data["gateway_id"]
        sensors_data = data["sensors"]
        if sensors_data:
            for sensor in sensors_data:
                schema = CreateSensorSchema(
                    name=sensor["name"],
                    mac_address=sensor["mac_address"],
                    type=sensor["type"],
                    gateway_device_id=gateway_id
                )
                await self.sensor_service.create(schema, session)

        connected_devices_data = data["connected_devices"]
        if connected_devices_data:
            for device in connected_devices_data: # ?? TODO
                schema = CreateConnectedDeviceSchema(
                    name=device["name"],
                    mac_address=device["mac_address"],
                    gateway_device_id=gateway_id,
                    priority=device["priority"]
                )
                await self.connected_device_service.create(schema, session)
