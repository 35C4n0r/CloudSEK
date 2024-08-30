from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: UUID
    username: str
    created_at: datetime
