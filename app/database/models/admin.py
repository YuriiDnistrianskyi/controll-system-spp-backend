from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, ForeignKey
from app.database.database import Base

class Admin(Base):
    __tablename__ = "admin"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[String] = mapped_column(String)
    last_name: Mapped[String] = mapped_column(String)
    email: Mapped[String] = mapped_column(String)
    password_hash: Mapped[String] = mapped_column(String)

    @staticmethod
    def create_from_dto(dto: dict) -> object:
        return Admin(**dto)
