from pydantic import BaseModel
from typing import Optional

class CreateSensorSchema(BaseModel):
    name: str
    mac_address: str
    type_id: int
    system_id: int

class UpdateSensorSchema(BaseModel):
    name: Optional[str] = None
    mac_address: Optional[str] = None
    type_id: Optional[int] = None #
    system_id: Optional[int] = None
