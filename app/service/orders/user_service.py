from sqlalchemy.ext.asyncio import AsyncSession

from app.service.base.base_service import BaseService
from app.database.models.user import User
from app.schemas.user_schemas import CreateUserSchema, UpdateUserSchema
from app.core.serurity import create_hash


class UserService(BaseService[User]):

    async def create(self, schema: CreateUserSchema, session: AsyncSession) -> User:
        obj = User(
            first_name=schema.first_name,
            last_name=schema.last_name,
            email=schema.email,
            password_hash=create_hash(schema.password),
        )

        await self.repository.add(obj, session)
        return obj


    async def update(self, id: int, schema: UpdateUserSchema, session: AsyncSession) -> User:
        obj = await self.repository.get_by_id(id, session)
        data_dict = schema.model_dump(exclude_unset=True)

        if 'first_name' in data_dict:
            obj.first_name = data_dict.get('first_name')

        if 'last_name' in data_dict:
            obj.last_name = data_dict.get('last_name')

        if 'email' in data_dict:
            obj.email = data_dict.get('email')

        return obj
