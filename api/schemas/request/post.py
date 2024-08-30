from uuid import UUID

from fastapi.openapi.models import Schema
from pydantic import BaseModel


class PostCreateRequest(BaseModel):
    title: str
    content: str
    user_id: UUID


class PostUpdateRequest(BaseModel):
    id: UUID
    title: str
    content: str
    user_id: UUID
