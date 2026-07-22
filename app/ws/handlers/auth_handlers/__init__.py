from app.ws.handlers.auth_handlers.authentication_handler import AuthenticationHandler
from app.ws.handlers.auth_handlers.initialization_handler import InitializationHandler
from app.service import gateway_device_service

authentication_handler = AuthenticationHandler(
    gateway_service=gateway_device_service
)

initialization_handler = InitializationHandler(
    gateway_service=gateway_device_service
)

