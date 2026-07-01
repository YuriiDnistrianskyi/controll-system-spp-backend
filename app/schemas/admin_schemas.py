from pydantic import BaseModel
from typing import Optional

class CreateAdmin(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class UpdateAdmin(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None

class UpdatePasswordAdmin(BaseModel):
    new_password: str
