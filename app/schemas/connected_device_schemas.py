from pydantic import BaseModel
from typing import Optional

class CreateConnectedDeviceSchema(BaseModel):
    name: str
    mac_address: str
    gateway_device_id: int
    priority: int

class UpdateConnectedDeviceSchema(BaseModel):
    name: Optional[str] = None
    mac_address: Optional[str] = None
    gateway_device_id: Optional[int] = None
    priority: Optional[int] = None
