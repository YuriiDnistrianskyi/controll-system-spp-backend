from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base


class DeviceType(Base):
    __tablename__ = "device_type"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[String] = mapped_column(String)

    @staticmethod
    def create_from_dto(dto: dict) -> object:
        return DeviceType(**dto)
