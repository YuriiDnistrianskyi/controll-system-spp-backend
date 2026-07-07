from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class RoleType(Base):
    __tablename__ = 'role_type'

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[String] = mapped_column(String, unique=True)
    type: Mapped[String] = mapped_column(String, unique=True)
