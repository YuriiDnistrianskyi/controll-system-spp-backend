from fastapi import FastAPI

from app.api.gateway_routes import gateway_router


def connect_routers(app: FastAPI):
    app.include_router(gateway_router, prefix="/api/gateway")
