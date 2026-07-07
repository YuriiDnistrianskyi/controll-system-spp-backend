from pydantic import BaseModel
from typing import Optional

class CreateConnectedDeviceSchema(BaseModel):
    name: str
    mac_address: str
    system_id: int
    priority: int

class UpdateConnectedDeviceSchema(BaseModel):
    name: Optional[str] = None
    mac_address: Optional[str] = None
    system_id: Optional[int] = None
    priority: Optional[int] = None
