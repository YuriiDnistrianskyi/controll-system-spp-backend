from app.ws.handlers.i_handler import IHandler


class Dispatcher:
    def __init__(self, snapshot_handler: IHandler, init_device_handler: IHandler):
        self.handlers = {
            'snapshot': snapshot_handler,
            'init_device': init_device_handler
        }
        self.snapshot_handler = snapshot_handler
        self.init_device_handler = init_device_handler

    async def dispatch(self, data: dict):
        msg_type = data['type']

        if msg_type in self.handlers:
            await self.handlers[msg_type].handle(data)
