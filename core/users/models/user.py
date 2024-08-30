from datetime import datetime

import pytz
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, TEXT
from sqlalchemy.dialects.postgresql import UUID, JSONB

from core.database.database import Base


class UserORM(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String(255), unique=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(pytz.UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(pytz.UTC))
