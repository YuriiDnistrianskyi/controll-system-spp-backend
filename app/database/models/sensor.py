from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base

class Sensor(Base):
    __tablename__ = "sensor"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    mac_address: Mapped[String] = mapped_column(String, unique=True)
    type_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("device_type.id"))
    system_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("system.id"))
