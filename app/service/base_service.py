from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generic, TypeVar

from app.repository.relational.base_repository import BaseRepository


T = TypeVar("T")

class BaseService(Generic[T]):

    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository


    async def get_all(self, session: AsyncSession) -> list[T]:
        return await self.repository.get_all(session)


    async def get_by_id(self, id: int, session: AsyncSession) -> T:
        return await self.repository.get_by_id(id, session)


    async def create(self, schema, session: AsyncSession) -> None:
        pass


    async def update(self, id: int, schema, session: AsyncSession) -> T:
        pass


    async def delete(self, id: int, session: AsyncSession) -> None:
        await self.repository.delete(id, session)
