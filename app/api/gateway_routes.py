from fastapi import APIRouter, WebSocket, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.ws import ws_manager
from app.database.dependencies import *
from app.ws import dispatcher


gateway_router = APIRouter()

@gateway_router.websocket("/ws/{mac_address}")
async def websocket_endpoint(
        websocket: WebSocket,
        mac_address: str,
        session_factory = Depends(get_session_factory)
):
    await ws_manager.connect(websocket, mac_address)

    gateway_id: int | None = None

    try:
        data = await websocket.receive()
        async with session_factory() as session:
            gateway_id = await dispatcher.authorize(data, session)
    except Exception as ex:
        print(f'Error: {ex}')
        await ws_manager.close(gateway_id=gateway_id, mac_address=mac_address)


    try:
        while True:
            data = await websocket.receive_json()
            async with session_factory() as session:
                await dispatcher.dispatch(data, session)
    except Exception as ex:
        print(f'Error: {ex}')
        await ws_manager.close(gateway_id=gateway_id)
