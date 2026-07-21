import asyncio
from pydantic import EmailStr

from app.service import user_service
from app.schemas.user_schemas import CreateUserSchema

from app.database.dependencies import get_async_session, get_session_factory

async def test() -> None:
    schema = CreateUserSchema(
        first_name='test',
        last_name='test',
        email='test@test.com',
        password='1111',
    )

    session_factory = get_session_factory()

    async with session_factory() as session:
        result = await user_service.create(schema, session)
        await session.commit()
        # print(result['token'])


if __name__ == "__main__":
    asyncio.run(test())
