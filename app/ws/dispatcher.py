from sqlalchemy.ext.asyncio import AsyncSession

from app.ws.handlers.i_handler import IHandler


class Dispatcher:
    def __init__(
            self,
            snapshot_handler: IHandler,
            init_device_handler: IHandler,
            authentication_handler: IHandler,
            initialization_handler: IHandler,
    ) -> None:
        self.handlers = {
            'snapshot': snapshot_handler,
            'init_device': init_device_handler
        }
        self.auth_handlers = {
            'authentication': authentication_handler,
            'initialization': initialization_handler,
        }

    async def dispatch(self, data: dict, session: AsyncSession) -> None:
        msg_type = data['type']

        if msg_type in self.handlers:
            await self.handlers[msg_type].handle(data, session)

    async def authenticate(self, data: dict, session: AsyncSession) -> int:
        msg_type = data['type']

        if msg_type in self.auth_handlers:
            gateway_id: int = await self.auth_handlers[msg_type].handle(data, session)
            return gateway_id
        else:
            raise Exception(f'Not find type {msg_type}')
