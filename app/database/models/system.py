from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from app.database.database import Base


class System(Base):
    __tablename__ = "system"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    owner_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('_user.id'))

    gateway_devices = relationship(
        "GatewayDevice",
        back_populates="system",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
