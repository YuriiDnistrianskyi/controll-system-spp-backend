import asyncio

from app.service import system_service
from app.schemas.system_schemas import CreateSystemSchema

from app.database.dependencies import get_async_session, get_session_factory

async def test() -> None:
    schema = CreateSystemSchema(
        name='test',
        owner_id=1
    )

    session_factory = get_session_factory()

    async with session_factory() as session:
        result = await system_service.create(schema, session)
        await session.commit()
        # print(result['token'])


if __name__ == "__main__":
    asyncio.run(test())
