from fastapi import FastAPI

from app.api import connect_routers


def create_app() -> FastAPI:
    app: FastAPI = FastAPI()
    connect_routers(app)
    return app
