from app.ws.ws_manager import WsManager
from app.ws.snapshot_handler import SnapshotHandler
from app.service import battery_telemetry_service, network_telemetry_service, sensor_telemetry_service

ws_manager = WsManager()

snapshot_handler = SnapshotHandler(
    battery_service=battery_telemetry_service,
    network_service=network_telemetry_service,
    sensor_service=sensor_telemetry_service,
)
