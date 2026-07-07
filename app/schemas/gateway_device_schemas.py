from pydantic import BaseModel
from typing import Optional

class CreateGatewayDeviceSchema(BaseModel):
    name: str
    mac_address: str
    system_id: int

class UpdateGatewayDeviceSchema(BaseModel):
    name: Optional[str] = None
    mac_address: Optional[str] = None
    system_id: Optional[int] = None

class UpdateTokenGatewayDeviceSchema(BaseModel):
    token: str
