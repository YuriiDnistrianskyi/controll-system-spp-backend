from app.service import TelemetryService
from app.ws.handlers.i_handler import IHandler


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

    async def handle(self, data):
        gateway_id = data["gateway_id"]

        battery_data = data["battery"]
        if battery_data:
            # battery_data["device_id"] = gateway_id # front_sensor_id | not gateway
            await self.battery_service.add(battery_data)

        network_data = data["network"]
        if network_data:
            network_data["device_id"] = gateway_id
            await self.network_service.add(network_data)

        sensor_data = data["sensor"]
        if sensor_data:
            for sensor in sensor_data:
                await self.sensor_service.add(sensor)
