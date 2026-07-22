from sqlalchemy.ext.asyncio import AsyncSession

from app.ws.handlers.auth_handlers.i_auth_handler import IAuthHandler
from app.service.orders.gateway_device_service import GatewayDeviceService
from app.schemas.gateway_device_schemas import InitGatewayDeviceSchema


class InitializationHandler(IAuthHandler):
    def __init__(self, gateway_service: GatewayDeviceService) -> None:
        self.gateway_service = gateway_service

    async def handle(self, data: dict, session: AsyncSession) -> int: #TODO
        schema = InitGatewayDeviceSchema(
            token=data['token'],
            mac_address=data['mac_address']
        )

        gateway_id: int = await self.gateway_service.initialize(schema, session)
        return gateway_id
