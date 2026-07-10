from app.repository.non_relational.base_non_relational_repository import BaseNonRelationalRepository

class BaskSensorRepository(BaseNonRelationalRepository):
    measurement: str = 'bask_sensor'
