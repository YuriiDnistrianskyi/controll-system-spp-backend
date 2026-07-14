from influxdb_client import Point
from typing import Any
import datetime

from app.repository.non_relational.base_non_relational_repository import BaseNonRelationalRepository


class TelemetryService:
    def __init__(self, repository: BaseNonRelationalRepository):
        self.repository = repository

    @staticmethod
    def create_point(measurement: str, data: dict) -> Point:
        point = Point(measurement)

        for key, value in data.items():
            if key == 'device_id':
                point.tag('device_id', value)
                continue
            point.field(key, value)

        point.time(datetime.datetime.now(datetime.timezone.utc)) # TODO

        return point

    async def get(self, device_id: int, field: str) -> list[dict[str, Any]]:
        return await self.repository.get(device_id, field)

    def get_last_record(self, device_id: int) -> dict[str, Any]:
        return  self.repository.get_last_record(device_id)

    def get_last_field(self, device_id: int, field: str) -> dict[str, Any]:
        return  self.repository.get_last_field(device_id, field)

    def add(self, point: Point) -> None:
         self.repository.add(point)

