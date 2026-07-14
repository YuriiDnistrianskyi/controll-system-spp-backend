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

# from app.database.models.connected_device import ConnectedDevice
from app.database.models.device_type import DeviceType
from app.database.models.gateway_device import GatewayDevice
from app.database.models.role_type import RoleType
from app.database.models.sensor import Sensor
from app.database.models.session import Session
from app.database.models.system import System
from app.database.models.user import User
from app.database.models.user_to_system import UserToSystem
