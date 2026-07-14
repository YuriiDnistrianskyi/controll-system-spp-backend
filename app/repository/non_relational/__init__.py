from app.repository.non_relational.battery_repository import BatteryRepository
from app.repository.non_relational.network_repository import NetworkRepository
from app.repository.non_relational.sensor_data_repository import SensorDataRepository

from app.database.influxdb import write_api, query_api


battery_repository = BatteryRepository(write_api, query_api)
network_repository = NetworkRepository(write_api, query_api)
sensor_data_repository = SensorDataRepository(write_api, query_api)
