from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class UpdateUserSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None

class UpdatePasswordUserSchema(BaseModel):
    new_password: str
