from app.repository.relational.base_repository import BaseRepository
from app.database.models.session import Session

class SessionRepository(BaseRepository[Session]):
    _model = Session
