from fastapi import APIRouter, WebSocket, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import json

from app.ws import ws_manager
from app.database.dependencies import *
from app.ws import dispatcher


gateway_router = APIRouter()

@gateway_router.websocket("/ws")
async def websocket_endpoint(
        websocket: WebSocket,
        session_factory = Depends(get_session_factory)
):
    mac_address: str = websocket.query_params.get('mac_address')

    await ws_manager.connect(websocket, mac_address)

    gateway_id: int | None = None


    try:
        data = await websocket.receive_text()
        payload = json.loads(data)

        async with session_factory() as session:
            gateway_id = await dispatcher.authenticate(payload, session)
    except Exception as ex:
        print(f'Error: {ex}')
        await ws_manager.close(gateway_id=gateway_id, mac_address=mac_address)

    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)

            async with session_factory() as session:
                await dispatcher.dispatch(payload, gateway_id, session)
    except Exception as ex:
        print(f'Error: {ex}')
        await ws_manager.close(gateway_id=gateway_id)
