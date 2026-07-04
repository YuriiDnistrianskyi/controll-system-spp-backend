from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base

class GatewayDevice(Base):
    __tablename__ = "gateway_device"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    token_hash: Mapped[String] = mapped_column(String, unique=True)
    mac_address: Mapped[String] = mapped_column(String, unique=True)
    system_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("system.id"))
