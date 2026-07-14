from influxdb_client import Point
from typing import Any

from app.core.config import INFLUXDB_BUCKET, INFLUXDB_ORG

class BaseNonRelationalRepository:
    _measurement: str | None = None

    def __init__(self, writer_api, query_api):
        self.__write_api = writer_api
        self.__query_api = query_api

    async def get_records(self, device_id: int, start: str = "-30d") -> list[dict[str, Any]]:
        query = f"""
                from(bucket: "{INFLUXDB_BUCKET}")
                |> range(start: {start})
                |> filter(fn: (r) =>
                    r._measurement == "{self._measurement}" and
                    r.device_id == "{device_id}"
                )
                """

        result: list = list()

        #TODO
        for table in self.__query_api.query(query, org=INFLUXDB_ORG):
            records = dict()
            for record in table.records:
                result.append(
                    {
                        'timestamp': "time",
                        str(record.get_field()): record.get_value()
                    }
                )
            result.append(records)

        return result

    async def get_fields(self, device_id: int, field: str) -> list[dict[str, Any]]:
        query = f"""
                from(bucket: "{INFLUXDB_BUCKET}")
                |> range(start: -30d)
                |> filter(fn: (r) =>
                    r._measurement == "{self._measurement}" and
                    r._field == "{field}" and
                    r.device_id == "{device_id}"
                )
                """

        result: list = list()

        for table in self.__query_api.query(query, org=INFLUXDB_ORG):
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
                    r._measurement == "{self._measurement}" and
                    r.device_id == "{device_id}"
                )
                |> last()
                """

        value: dict[str, Any] = dict()

        for table in self.__query_api.query(query, org=INFLUXDB_ORG):
            for record in table.records:
                value['timestamp'] = record.get_time() #TODO
                value[record.get_field()] = record.get_value()

        return value

    async def get_last_field(self, device_id: int, field: str) -> dict[str, Any]:
        query = f"""
                from(bucket: "{INFLUXDB_BUCKET}")
                |> range(start: -30d)
                |> filter(fn: (r) =>
                    r._measurement == "{self._measurement}" and
                    r._field == "{field}" and
                    r.device_id == "{device_id}"
                )
                |> last()
                """

        value: dict | None = None

        for table in self.__query_api.query(query, org=INFLUXDB_ORG):
            for record in table.records:
                value = {
                    'timestamp': record.get_time(),
                    record.get_field(): record.get_value()
                }

        return value

    async def add(self, point: Point) -> None:
        self.__write_api.write(
            bucket=INFLUXDB_BUCKET,
            org=INFLUXDB_ORG,
            record=point
        )

    async def remove(self):
        pass
