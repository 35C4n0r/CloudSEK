from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[UUID] = None
    username: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
