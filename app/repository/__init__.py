from app.repository.orders.admin_repository import AdminRepository
from app.repository.orders.connected_device_repository import ConnectedDeviceRepository
from app.repository.orders.device_type_repository import DeviceTypeRepository
from app.repository.orders.observer_repository import ObserverRepository
from app.repository.orders.system_repository import SystemRepository
from app.repository.orders.system_device_repository import SystemDeviceRepository
from app.repository.orders.system_to_observer_repository import SystemToObserverRepository

admin_repository = AdminRepository()
connected_device_repository = ConnectedDeviceRepository()
device_type_repository = DeviceTypeRepository()
observer_repository = ObserverRepository()
system_repository = SystemRepository()
system_device_repository = SystemDeviceRepository()
system_to_observer_repository = SystemToObserverRepository()
