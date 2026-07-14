from app.repository.non_relational.battery_repository import BatteryRepository
from app.repository.non_relational.network_repository import NetworkRepository
from app.repository.non_relational.sensor_data_repository import SensorDataRepository

battery_repository = BatteryRepository()
network_repository = NetworkRepository()
sensor_data_repository = SensorDataRepository()
