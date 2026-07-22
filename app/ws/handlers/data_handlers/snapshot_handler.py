from sqlalchemy.ext.asyncio import AsyncSession

from app.service import TelemetryService
from app.ws.handlers.data_handlers.i_handler import IHandler


class SnapshotHandler(IHandler):
    def __init__(
            self,
            battery_service: TelemetryService,
            network_service: TelemetryService,
            sensor_service: TelemetryService,
    ):
        self.battery_service = battery_service
        self.network_service = network_service
        self.sensor_service = sensor_service

    async def handle(self, data, gateway_id: int, session: AsyncSession):
        network_data = data.get("network")
        if network_data:
            network_data["device_id"] = gateway_id
            await self.network_service.add(network_data)

        battery_data = data.get("battery")
        if battery_data:
            for battery in battery_data:
                await self.battery_service.add(battery)

        sensor_data = data.get("sensor")
        if sensor_data:
            for sensor in sensor_data:
                await self.sensor_service.add(sensor)
