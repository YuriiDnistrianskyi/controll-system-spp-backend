from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.engine import Base

class Session(Base):
    __tablename__ = 'session'

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('_user.id'))
    token_hash: Mapped[String] = mapped_column(String)
    ip_address: Mapped[String] = mapped_column(String)
    created_time: Mapped[DateTime] = mapped_column(DateTime)
    expires_time: Mapped[DateTime] = mapped_column(DateTime)
    last_activity_time: Mapped[DateTime] = mapped_column(DateTime)
    is_active: Mapped[Boolean] = mapped_column(Boolean)
