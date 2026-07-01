from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base

class SystemToObserver(Base):
    __tablename__ = "system_to_observer"

    system_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("system.id"), primary_key=True)
    observer_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("observer.id"), primary_key=True)

    @staticmethod
    def create_from_dto(dto: dict) -> object:
        return SystemToObserver(**dto)
