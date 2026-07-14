from app.repository.non_relational.base_non_relational_repository import BaseNonRelationalRepository

class BatteryRepository(BaseNonRelationalRepository):
    measurement: str = 'battery'
