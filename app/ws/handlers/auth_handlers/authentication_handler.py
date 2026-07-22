from sqlalchemy.ext.asyncio import AsyncSession

from app.service.orders.gateway_device_service import GatewayDeviceService
from app.schemas.gateway_device_schemas import AuthGatewayDeviceSchema
from app.ws.handlers.auth_handlers.i_auth_handler import IAuthHandler


class AuthenticationHandler(IAuthHandler):
    def __init__(self, gateway_service: GatewayDeviceService):
        self.gateway_service = gateway_service

    async def handle(self, data: dict, session: AsyncSession) -> int:
        schema = AuthGatewayDeviceSchema(
            id=data['gateway_id'],
            token=data['token']
        )

        gateway_id: int = await self.gateway_service.authenticate(schema, session)
        return gateway_id
