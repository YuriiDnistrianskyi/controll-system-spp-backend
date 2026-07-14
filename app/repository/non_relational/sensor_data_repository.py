from app.repository.non_relational.base_non_relational_repository import BaseNonRelationalRepository

class SensorDataRepository(BaseNonRelationalRepository):
    measurement: str = 'sensor'
