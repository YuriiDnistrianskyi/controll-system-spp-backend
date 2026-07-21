from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.engine import Base

class GatewayDevice(Base):
    __tablename__ = "gateway_device"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    token_hash: Mapped[String] = mapped_column(String, unique=True)
    token_lookup: Mapped[String] = mapped_column(String)
    mac_address: Mapped[String] = mapped_column(String, unique=True, nullable=True)
    system_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("system.id", ondelete="CASCADE"))

    system = relationship("System", back_populates="gateway_devices")

    connected_devices = relationship(
        "ConnectedDevice",
        back_populates="gateway_device",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    sensors = relationship(
        "Sensor",
        back_populates="gateway_device",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
