from typing import Optional
from uuid import UUID

from fastapi.openapi.models import Schema
from pydantic import BaseModel


class CommentCreateRequest(BaseModel):
    content: str
    user_id: UUID
    is_child_comment: bool
    parent_id: Optional[UUID] = None
    post_id: UUID


class CommentUpdateRequest(BaseModel):
    id: UUID
    comment: str
    user_id: UUID
    is_child_comment: bool
    parent_id: Optional[UUID]
    post_id: UUID
