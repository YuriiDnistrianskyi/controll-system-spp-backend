from sqlalchemy.ext.asyncio import AsyncSession

from app.service.base_service import BaseService
from app.repository.base_repository import BaseRepository
from app.repository.orders.user_to_system_repository import UserToSystemRepository
from app.repository.orders.role_type_repository import RoleTypeRepository
from app.database.models.system import System
from app.database.models.user_to_system import UserToSystem
from app.schemas.system_schemas import CreateSystemSchema, UpdateSystemSchema


class SystemService(BaseService[System]):

    def __init__(self,
                 repository: BaseRepository[System],
                 user_to_system_repository: UserToSystemRepository,
                 role_type_repository: RoleTypeRepository
        ):
        super().__init__(repository)
        self.user_to_system_repository = user_to_system_repository
        self.role_type_repository = role_type_repository

    async def create(self, schema: CreateSystemSchema, session: AsyncSession) -> System:
        obj = System(
            name=schema.name,
            owner_id=schema.owner_id,
        )

        await self.repository.add(obj, session)
        # await session.commit()
        await session.refresh(obj)

        admin_id: int = await self.role_type_repository.get_admin_type_id(session)
        user_to_system = UserToSystem(
            user_id=schema.owner_id,
            system_id=obj.id,
            role_id=admin_id,
        )

        await self.user_to_system_repository.add(user_to_system, session)

        return obj

    async def update(self, id: int, schema: UpdateSystemSchema, session: AsyncSession) -> System:
        obj = await self.repository.get_by_id(id, session)
        data_dict = schema.model_dump(exclude_unset=True)

        if 'name' in data_dict:
            obj.name = data_dict['name']

        if 'owner_id' in data_dict:
            obj.owner_id = data_dict['owner_id']

        return obj

    async def delete(self, id: int, session: AsyncSession) -> None:
        super().delete(id, session)
        #TODO

