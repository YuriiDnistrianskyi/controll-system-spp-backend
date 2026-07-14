from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.engine import Base

class Sensor(Base):
    __tablename__ = "sensor"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    mac_address: Mapped[String] = mapped_column(String, unique=True)
    type_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("device_type.id"))
    gateway_device_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("gateway_device.id", ondelete="CASCADE"))

    gateway_device = relationship(
        "GatewayDevice",
        back_populates="sensors",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
