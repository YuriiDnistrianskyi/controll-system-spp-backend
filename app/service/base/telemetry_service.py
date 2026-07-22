from influxdb_client import Point
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
import datetime

from app.repository.non_relational.base_non_relational_repository import BaseNonRelationalRepository


class TelemetryService:
    def __init__(self, repository: BaseNonRelationalRepository):
        self._repository = repository
        self._measurement = repository.get_measurement()

    async def _create_point(self, data: dict) -> Point:
        point = Point(self._measurement)

        for key, value in data.items():
            if key == 'device_id':
                point.tag('device_id', value)
                continue
            point.field(key, value)

        point.time(datetime.datetime.now(datetime.timezone.utc)) # TODO

        return point

    async def get_records(self, device_id: int) -> list[dict[str, Any]]:
        return await self._repository.get_records(device_id)

    async def get_fields(self, device_id: int, field: str) -> list[dict[str, Any]]:
        return await self._repository.get_fields(device_id, field)

    async def get_last_record(self, device_id: int) -> dict[str, Any]:
        return await self._repository.get_last_record(device_id)

    async def get_last_field(self, device_id: int, field: str) -> dict[str, Any]:
        return await self._repository.get_last_field(device_id, field)

    async def add(self, data: dict, session: AsyncSession=None) -> None:
        point: Point = await self._create_point(data)
        await self._repository.add(point)

