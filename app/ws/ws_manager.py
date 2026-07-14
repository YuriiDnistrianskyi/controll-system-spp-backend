from fastapi import WebSocket

class WsManager:
    def __init__(self):
        self.connections: dict[int, WebSocket] = {}

    async def connect(self, gateway_device_id: int, ws: WebSocket):
        await ws.accept()
        self.connections[gateway_device_id] = ws

    async def send(self, gateway_device_id: int, data: dict):
        ws = self.connections[gateway_device_id]
        if ws:
            await ws.send_json(data)

    async def close(self, gateway_device_id: int):
        self.connections.pop(gateway_device_id)
