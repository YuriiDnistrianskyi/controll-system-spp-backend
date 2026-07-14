from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.engine import Base


class UserToSystem(Base):
    __tablename__ = 'user_to_system'

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('_user.id'))
    system_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('system.id', ondelete="CASCADE"))
    role_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('role_type.id'))
