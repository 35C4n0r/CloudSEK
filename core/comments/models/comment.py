from datetime import datetime

import pytz
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, TEXT, BOOLEAN
from sqlalchemy.dialects.postgresql import UUID, JSONB

from core.database.database import Base


class CommentORM(Base):
    __tablename__ = "comments"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    # html_content = Column(TEXT, nullable=False)
    # json_content = Column(JSONB, nullable=False)
    content = Column(TEXT, nullable=False)
    is_child_comment = Column(BOOLEAN, nullable=False, default=False)
    parent_id = Column(UUID, ForeignKey("comments.id", ondelete="CASCADE"), nullable=True)
    post_id = Column(UUID, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(pytz.UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(pytz.UTC))
