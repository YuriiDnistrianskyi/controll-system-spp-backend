from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass

from app.database.models.admin import Admin
from app.database.models.connected_device import ConnectedDevice
from app.database.models.device_type import DeviceType
from app.database.models.observer import Observer
from app.database.models.system import System
from app.database.models.system_device import SystemDevice
from app.database.models.system_to_observer import SystemToObserver
