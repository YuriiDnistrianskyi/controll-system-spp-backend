import asyncio

from app.service import gateway_device_service
from app.schemas.gateway_device_schemas import CreateGatewayDeviceSchema

from app.database.dependencies import get_async_session, get_session_factory


data = {
    'device_id': 2,
    'power': 4,
    'strum': 6,
}

async def test() -> None:
    schema = CreateGatewayDeviceSchema(
        name='test',
        system_id=6
    )

    session_factory = get_session_factory()

    async with session_factory() as session:
        result = await gateway_device_service.create(schema, session)
        await session.commit()
        print(result['token'])

if __name__ == "__main__":
    asyncio.run(test())
