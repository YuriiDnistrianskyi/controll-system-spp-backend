from sqlalchemy.ext.asyncio import AsyncSession

from app.service.base_service import BaseService
from app.database.models.admin import Admin
from app.schemas.admin_schemas import CreateAdmin, UpdateAdmin, UpdatePasswordAdmin
from app.core.serurity import create_hashed_password


class AdminService(BaseService[Admin]):
    async def create(self, schema: CreateAdmin, session: AsyncSession) -> None:
        admin = Admin(
            first_name=schema.first_name,
            last_name=schema.last_name,
            email=schema.email,
            password_hash=create_hashed_password(schema.password),
        )

        await self.repository.add(admin, session)

    async def update(self, id: int, schema: UpdateAdmin, session: AsyncSession) -> Admin:
        admin = await self.repository.get_by_id(id, session)
        data_dict = schema.model_dump(exclude_unset=True)

        if 'first_name' in data_dict:
            admin.first_name = data_dict.get('first_name')

        if 'last_name' in data_dict:
            admin.last_name = data_dict.get('last_name')

        if 'email' in data_dict:
            admin.email = data_dict.get('email')

        return admin

    # async def update_password(self):
    #     pass
