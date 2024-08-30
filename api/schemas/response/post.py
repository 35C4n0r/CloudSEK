import uuid
from datetime import datetime

from pydantic import BaseModel


class PostResponse(BaseModel):
    id: uuid.UUID
    title: str
    content: str
    user_id: uuid.UUID
    updated_at: datetime
