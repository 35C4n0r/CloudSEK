from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.orm import Session


class CRUDModel(BaseModel):
    session: Optional[Session]
    workflow_id: Optional[UUID]

    class Config:
        arbitrary_types_allowed = True
