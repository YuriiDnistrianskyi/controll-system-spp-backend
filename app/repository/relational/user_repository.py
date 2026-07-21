from app.repository.relational.base_repository import BaseRepository
from app.database.models.user import User

class UserRepository(BaseRepository[User]):
    _model = User
