from pydantic import BaseModel
from typing import Optional

class CreateSystemSchema(BaseModel):
    name: str
    owner_id: int

class UpdateSystemSchema(BaseModel):
    name: Optional[str] = None
    owner_id: Optional[str] = None

class ManageObserverSchema(BaseModel):
    user_id: int
    system_id: int
