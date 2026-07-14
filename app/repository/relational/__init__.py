from app.repository.relational.connected_device_repository import ConnectedDeviceRepository
from app.repository.relational.device_type_repository import DeviceTypeRepository
from app.repository.relational.gateway_device_repository import GatewayDeviceRepository
from app.repository.relational.role_type_repository import RoleTypeRepository
from app.repository.relational.sensor_repository import SensorRepository
from app.repository.relational.session_repository import SessionRepository
from app.repository.relational.system_repository import SystemRepository
from app.repository.relational.user_repository import UserRepository
from app.repository.relational.user_to_system_repository import UserToSystemRepository

connected_device_repository = ConnectedDeviceRepository()
device_type_repository = DeviceTypeRepository()
gateway_device_repository = GatewayDeviceRepository()
role_type_repository = RoleTypeRepository()
sensor_repository = SensorRepository()
session_repository = SessionRepository()
system_repository = SystemRepository()
user_repository = UserRepository()
user_to_system_repository = UserToSystemRepository()
