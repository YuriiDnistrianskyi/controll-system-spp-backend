from app.ws.ws_manager import WsManager
from app.ws.dispatcher import Dispatcher
from app.ws.handlers import snapshot_handler, init_device_handler


ws_manager = WsManager()
dispatcher = Dispatcher(
    snapshot_handler,
    init_device_handler
)
