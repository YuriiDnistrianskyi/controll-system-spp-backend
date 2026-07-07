from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base


class ConnectedDevice(Base):
    __tablename__ = "connected_device"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    mac_address: Mapped[String] = mapped_column(String, unique=True)
    gateway_device_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("gateway_device.id", ondelete="CASCADE"))
    priority: Mapped[Integer] = mapped_column(Integer)

    gateway_device = relationship("GatewayDevice", back_populates="connected_devices")
