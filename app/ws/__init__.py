from app.ws.ws_manager import WsManager
from app.ws.dispatcher import Dispatcher
from app.ws.handlers import snapshot_handler, init_device_handler, authentication_handler, initialize_handler, \
    initialization_handler

ws_manager = WsManager()

dispatcher = Dispatcher(
    snapshot_handler=snapshot_handler,
    init_device_handler=init_device_handler,
    authorization_handler=authentication_handler,
    initialization_handler=initialization_handler,
)
