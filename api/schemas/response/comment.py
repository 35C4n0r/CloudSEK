import datetime
from uuid import UUID

from pydantic import BaseModel


class CommentResponse(BaseModel):
    id: UUID
    content: str
    user_id: UUID
    post_id: UUID
    updated_at: datetime.datetime
