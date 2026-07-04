from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateUserSchemas(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class UpdateUserSchemas(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None

class UpdatePasswordUserSchemas(BaseModel):
    new_password: str
