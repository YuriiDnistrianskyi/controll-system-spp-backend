from app.repository.non_relational.base_non_relational_repository import BaseNonRelationalRepository

class FrontSensorRepository(BaseNonRelationalRepository):
    measurement: str = 'front_sensor'
