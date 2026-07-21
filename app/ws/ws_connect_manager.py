from fastapi import WebSocket

class WsManager:
    def __init__(self):
        self.connections: dict[str, WebSocket] = {}
        self.auth_connections: dict[int, WebSocket] ={}

    async def connect(self, ws: WebSocket, mac_address: str):
        await ws.accept()
        self.connections[mac_address] = ws

    async def switch(self, mac_address: str, gateway_id: int):
        self.auth_connections[gateway_id] = self.connections[mac_address]
        self.connections.pop(mac_address)

    async def send(self, gateway_id: int, data: dict):
        ws = self.auth_connections[gateway_id]
        if ws:
            await ws.send_json(data)

    async def close(self, gateway_id: int=None, mac_address: str=None):
        if gateway_id and gateway_id in self.auth_connections:
            self.auth_connections.pop(gateway_id)

        if mac_address and mac_address in self.connections:
            self.connections.pop(mac_address)
