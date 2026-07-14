from influxdb_client import Point
from typing import Any

from app.core.config import INFLUXDB_BUCKET, INFLUXDB_ORG

class BaseNonRelationalRepository:
    measurement: str | None = None

    def __init__(self, writer_api, query_api):
        self.write_api = writer_api
        self.query_api = query_api

    async def get(self, device_id: int, field: str) -> list[dict[str, Any]]:
        query = f"""
                from(bucket: "{INFLUXDB_BUCKET}")
                |> range(start: -30d)
                |> filter(fn: (r) =>
                    r._measurement == "{self.measurement}" and
                    r._field == "{field}" and
                    r.device_id == "{device_id}"
                )
                """

        result: list = list()

        for table in self.query_api.query(query, org=INFLUXDB_ORG):
            for record in table.records:
                result.append(
                    {
                        'timestamp': record.get_time(),
                        record.get_field(): record.get_value()
                    }
                )

        return result

    async def get_last_record(self, device_id: int) -> dict[str, Any]:
        query = f"""
                from(bucket: "{INFLUXDB_BUCKET}")
                |> range(start: -30d)
                |> filter(fn: (r) =>
                    r._measurement == "{self.measurement}" and
                    r.device_id == "{device_id}"
                )
                |> last()
                """

        value: dict[str, Any] = dict()

        for table in self.query_api.query(query, org=INFLUXDB_ORG):
            for record in table.records:
                value['timestamp'] = record.get_time() #TODO
                value[record.get_field()] = record.get_value()

        return value

    async def get_last_field(self, device_id: int, field: str) -> dict[str, Any]:
        query = f"""
                from(bucket: "{INFLUXDB_BUCKET}")
                |> range(start: -30d)
                |> filter(fn: (r) =>
                    r._measurement == "{self.measurement}" and
                    r._field == "{field}" and
                    r.device_id == "{device_id}"
                )
                |> last()
                """

        value: dict | None = None

        for table in self.query_api.query(query, org=INFLUXDB_ORG):
            for record in table.records:
                value = {
                    'timestamp': record.get_time(),
                    record.get_field(): record.get_value()
                }

        return value

    async def add(self, point: Point) -> None:
        self.write_api.write(
            bucket=INFLUXDB_BUCKET,
            org=INFLUXDB_ORG,
            record=point
        )

    async def remove(self):
        pass
