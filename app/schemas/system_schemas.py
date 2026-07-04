from pydantic import BaseModel
from typing import Optional

class CreateSystemSchema(BaseModel):
    name: str
    owner_id: int

class UpdateSystemSchema(BaseModel):
    name: Optional[str] = None
    owner_id: Optional[str] = None
