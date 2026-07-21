from app.repository.relational.base_repository import BaseRepository
from app.database.models.system import System

class SystemRepository(BaseRepository[System]):
    _model = System
