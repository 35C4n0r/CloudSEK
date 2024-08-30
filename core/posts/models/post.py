from datetime import datetime
import pytz
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, TEXT
from sqlalchemy.dialects.postgresql import UUID, JSONB

from core.database.database import Base


class PostORM(Base):
    __tablename__ = 'posts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    content = Column(TEXT, nullable=False)
    title = Column(TEXT, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(pytz.UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(pytz.UTC))

