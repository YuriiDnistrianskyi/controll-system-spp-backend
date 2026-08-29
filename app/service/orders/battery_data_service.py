from sqlalchemy.ext.asyncio import AsyncSession

from app.service.base.telemetry_service import TelemetryService


class BatteryDataService(TelemetryService):
    async def add(self, data: dict, session: AsyncSession=None) -> None:
        await super().add(data)

        if session is None:
            return

        charge_level = data.get('charge_level')
        if charge_level and charge_level < 20:
            pass
