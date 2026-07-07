from app.repository.orders.connected_device_repository import ConnectedDeviceRepository
from app.repository.orders.device_type_repository import DeviceTypeRepository
from app.repository.orders.gateway_device_repository import GatewayDeviceRepository
from app.repository.orders.role_type_repository import RoleTypeRepository
from app.repository.orders.sensor_repository import SensorRepository
from app.repository.orders.session_repository import SessionRepository
from app.repository.orders.system_repository import SystemRepository
from app.repository.orders.user_repository import UserRepository
from app.repository.orders.user_to_system_repository import UserToSystemRepository

connected_device_repository = ConnectedDeviceRepository()
device_type_repository = DeviceTypeRepository()
gateway_device_repository = GatewayDeviceRepository()
role_type_repository = RoleTypeRepository()
sensor_repository = SensorRepository()
session_repository = SessionRepository()
system_repository = SystemRepository()
user_repository = UserRepository()
user_to_system_repository = UserToSystemRepository()
