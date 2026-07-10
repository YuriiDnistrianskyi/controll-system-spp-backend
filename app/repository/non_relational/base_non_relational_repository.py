from influxdb_client import Point
from typing import Any

from app.core.config import INFLUXDB_BUCKET, INFLUXDB_ORG
from app.database.influxdb import client, write_api, query_api

class BaseNonRelationalRepository:
    measurement: str | None = None

    async def get(self, device_id: int, field: str) -> list[dict[str, Any]]:
        query = f"""
            from(bucket:{INFLUXDB_BUCKET})
            |> range(start: -30d)
            |> filter(fn: (r) =>
                r._measurement == {self.measurement} and
                r._field == "{field}" and
                r.device_id == "{device_id}"
            )
        """

        result: list = list()

        for table in query_api.query(query, org=INFLUXDB_ORG):
            for record in table.records:
                result.append(
                    {
                        'timestamp': record.get_time(),
                        'value': record.get_value()
                    }
                )

        return result

    async def get_last(self, device_id: int, field: str) -> dict[str, Any]:
        query = f"""
            from(bucket:{INFLUXDB_BUCKET}
            |> filter(fn: (r) =>
                r._measurement == {self.measurement} and
                r._field == "{field}" and
                r.device_id == "{device_id}
            |> last()
        """

        value: dict | None = None

        for record in query_api.query(query, org=INFLUXDB_ORG):
            value = {
                'timestamp': record.get_time(),
                'value': record.get_value()
            }

        return value

    async def add(self, point: Point) -> None:
        write_api.write(
            bucket=INFLUXDB_BUCKET,
            org=INFLUXDB_ORG,
            record=point
        )

    def remove(self):
        pass
