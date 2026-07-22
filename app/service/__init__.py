from app.service.orders.connected_device_service import ConnectedDeviceService
from app.service.orders.gateway_device_service import GatewayDeviceService
from app.service.orders.sensor_service import SensorService
from app.service.orders.session_service import SessionService
from app.service.orders.system_service import SystemService
from app.service.orders.user_service import UserService

from app.repository.relational import *

from app.service.orders.battery_data_service import BatteryDataService
from app.service.orders.network_data_service import NetworkDataService
from app.service.orders.sensor_data_service import SensorDataService

from app.repository.non_relational import *

connected_device_service = ConnectedDeviceService(connected_device_repository)
gateway_device_service = GatewayDeviceService(gateway_device_repository)
sensor_service = SensorService(sensor_repository, device_type_repository)
session_service = SessionService(session_repository)
system_service = SystemService(system_repository, user_to_system_repository, role_type_repository)
user_service = UserService(user_repository)

battery_telemetry_service = BatteryDataService(battery_repository)
network_telemetry_service = NetworkDataService(network_repository)
sensor_telemetry_service = SensorDataService(sensor_data_repository)
