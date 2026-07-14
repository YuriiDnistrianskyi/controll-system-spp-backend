from pydantic import BaseModel
from typing import Optional

class CreateSensorSchema(BaseModel):
    name: str
    mac_address: str
    type: str
    gateway_device_id: int

class UpdateSensorSchema(BaseModel):
    name: Optional[str] = None
    mac_address: Optional[str] = None
    type: Optional[str] = None #
    gateway_device_id: Optional[int] = None
