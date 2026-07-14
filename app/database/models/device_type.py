from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.engine import Base


class DeviceType(Base):
    __tablename__ = "device_type"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[String] = mapped_column(String, unique=True)
    type: Mapped[String] = mapped_column(String, unique=True)

    @staticmethod
    def create_from_dto(dto: dict) -> object:
        return DeviceType(**dto)
