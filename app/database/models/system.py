from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, ForeignKey
from app.database.database import Base


class System(Base):
    __tablename__ = "system"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    admin_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('admin.id'))


    @staticmethod
    def create_from_dto(dto: dict) -> object:
        return System(**dto)
