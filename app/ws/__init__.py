from app.ws.ws_connect_manager import WsManager

ws_manager = WsManager()


from app.ws.dispatcher import Dispatcher
from app.ws.handlers import snapshot_handler, init_device_handler, authentication_handler, initialization_handler, \
    initialization_handler

dispatcher = Dispatcher(
    snapshot_handler=snapshot_handler,
    init_device_handler=init_device_handler,
    authentication_handler=authentication_handler,
    initialization_handler=initialization_handler,
)
