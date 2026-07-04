from sqlalchemy.ext.asyncio import AsyncSession

from app.service.base_service import BaseService
from app.database.models.session import Session
from app.schemas.session_schemas import CreateSessionSchema, UpdateSessionSchema
from app.core.serurity import create_hash


class SessionService(BaseService[Session]):
    pass

    async def create(self, schema: CreateSessionSchema, session: AsyncSession) -> Session:
        obj = Session(
            user_id=schema.user_id,
            token_hash=create_hash(schema.token),
            ip_address=schema.ip_address,
            create_time=schema.create_time,
            expires_time=schema.expires_time,
            last_activity_time=schema.last_activity_time,
            is_active=schema.is_active
        )

        await self.repository.add(obj, session)
        return obj

    async def update(self, id: int, schema: UpdateSessionSchema, session: AsyncSession) -> Session:
        obj = await self.repository.get_by_id(id, session)
        data_dict = schema.model_dump(exclude_unset=True)

        if 'ip_address' in data_dict:
            obj.ip_address = data_dict['ip_address']

        if 'expires_time' in data_dict:
            obj.expires_time = data_dict['expires_time']

        if 'last_activity_time' in data_dict:
            obj.last_activity_time = data_dict['last_activity_time']
            # obj.expire_time = ...

        if 'is_active' in data_dict:
            obj.is_active = False #

        return obj