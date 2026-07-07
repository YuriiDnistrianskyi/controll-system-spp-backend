from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CreateSessionSchema(BaseModel):
    user_id: int
    token: str #
    ip_address: str
    create_time: datetime
    expires_time: datetime #
    last_activity_time: datetime #
    is_active: bool

class UpdateSessionSchema(BaseModel):
    ip_address: Optional[str] = None
    expires_time: Optional[datetime] = None
    last_activity_time: Optional[datetime] = None
    is_active: Optional[bool] = None
