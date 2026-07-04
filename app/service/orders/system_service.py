from sqlalchemy.ext.asyncio import AsyncSession

from app.service.base_service import BaseService
from app.database.models.system import System
from app.schemas.system_schemas import CreateSystemSchema, UpdateSystemSchema


class SystemService(BaseService[System]):
    async def create(self, schema: CreateSystemSchema, session: AsyncSession) -> System:
        obj = System(
            name=schema.name,
            owner_id=schema.owner_id,
        )

        await self.repository.add(obj, session)
        return obj

    async def update(self, id: int, schema: UpdateSystemSchema, session: AsyncSession) -> System:
        obj = await self.repository.get_by_id(id, session)
        data_dict = schema.model_dump(exclude_unset=True)

        if 'name' in data_dict:
            obj.name = data_dict['name']

        if 'owner_id' in data_dict:
            obj.owner_id = data_dict['owner_id']

        return obj
