import asyncio

from app.service import sensor_telemetry_service

data = {
    'device_id': 2,
    'power': 4,
    'strum': 6,
}

async def test() -> None:
    # await sensor_telemetry_service.add(data)
    #
    # result = await sensor_telemetry_service.get_records(2)
    # print(result)

    for device in data:
        print(device)


if __name__ == "__main__":
    asyncio.run(test())
