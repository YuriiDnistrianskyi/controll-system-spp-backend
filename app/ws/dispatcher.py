from sqlalchemy.ext.asyncio import AsyncSession

from app.ws.handlers.i_handler import IHandler


class Dispatcher:
    def __init__(
            self,
            snapshot_handler: IHandler,
            init_device_handler: IHandler,
            authorization_handler: IHandler,
            initialization_handler: IHandler,
    ) -> None:
        self.handlers = {
            'snapshot': snapshot_handler,
            'init_device': init_device_handler
        }
        self.auth_handlers = {
            'authorization': authorization_handler,
            'initialization': initialization_handler,
        }

    async def dispatch(self, data: dict, session: AsyncSession) -> None:
        msg_type = data['type']

        if msg_type in self.handlers:
            await self.handlers[msg_type].handle(data, session)

    async def authorize(self, data: dict, session: AsyncSession) -> int:
        msg_type = data['type']

        if msg_type in self.auth_handlers:
            gateway_id: int = await self.auth_handlers[msg_type].handle(data, session)
        else:
            raise Exception('Authorization error')
