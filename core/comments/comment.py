from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Comment(BaseModel):
    id: Optional[UUID] = None
    user_id: UUID
    content: str
    is_child_comment: bool
    parent_id: Optional[UUID] = None
    post_id: UUID
    username: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        # orm_mode = True
        from_attributes = True
