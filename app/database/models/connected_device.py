from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base


class ConnectedDevice(Base):
    __tablename__ = "connected_device"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    mac_address: Mapped[String] = mapped_column(String, unique=True)
    system_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("system.id"))
    priority: Mapped[Integer] = mapped_column(Integer)

    code: Mapped[String] = mapped_column(String, unique=True) #
    password_hash: Mapped[String] = mapped_column(String) #

    @staticmethod
    def create_from_dto(dto: dict) -> object:
        return ConnectedDevice(**dto)
