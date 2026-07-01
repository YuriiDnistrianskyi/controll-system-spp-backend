from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base

class SystemDevice(Base):
    __tablename__ = "system_device"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    code: Mapped[String] = mapped_column(String, unique=True)
    mac_address: Mapped[String] = mapped_column(String, unique=True)
    password_hash: Mapped[String] = mapped_column(String)
    type_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("device_type.id"))
    system_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("system.id"))

    @staticmethod
    def create_from_dto(dto: dict) -> object:
        return SystemDevice(**dto)
