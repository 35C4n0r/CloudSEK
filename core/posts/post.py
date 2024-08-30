from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Post(BaseModel):
    id: Optional[UUID] = None
    user_id: UUID
    title: str
    content: str
    username: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
