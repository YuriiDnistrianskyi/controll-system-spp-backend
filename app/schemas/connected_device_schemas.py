from pydantic import BaseModel
from typing import Optional

class CreateConnectedDevice(BaseModel):
    name: str
    mac_address: str
    system_id: int
    priority: int

class UpdateConnectedDevice(BaseModel):
    name: Optional[str] = None
    mac_address: Optional[str] = None
    system_id: Optional[int] = None
    priority: Optional[int] = None
