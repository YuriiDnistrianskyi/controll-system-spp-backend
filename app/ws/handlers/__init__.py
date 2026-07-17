from app.ws.handlers.snapshot_handler import SnapshotHandler
from app.ws.handlers.init_device_handler import InitDeviceHandler
from app.ws.handlers.authentication_handler import AuthenticationHandler
from app.ws.handlers.initialization_handler import InitializationHandler
from app.service import battery_telemetry_service, network_telemetry_service, sensor_telemetry_service, sensor_service, connected_device_service, gateway_device_service

snapshot_handler = SnapshotHandler(
    battery_service=battery_telemetry_service,
    network_service=network_telemetry_service,
    sensor_service=sensor_telemetry_service,
)

init_device_handler = InitDeviceHandler(
    sensor_service=sensor_service,
    connected_device_service=connected_device_service,
)

authorize_handler = AuthenticationHandler(
    gateway_service=gateway_device_service
)

initialize_handler = InitializationHandler(
    gateway_service=gateway_device_service
)

