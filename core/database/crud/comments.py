import uuid
from datetime import datetime

import pytz

from core.comments.comment import Comment
from core.comments.models.comment import CommentORM
from core.database.connection import LocalSession
from core.database.crud.base import CRUDModel
from core.utils.exceptions.integrity import DoesNotExistException


class CommentCRUD(CRUDModel):

    @staticmethod
    def create_comment(comment: Comment) -> Comment:
        comment_id = uuid.uuid4()
        db_comment = CommentORM(id=comment_id, user_id=comment.user_id, content=comment.content,
                                is_child_comment=comment.is_child_comment, parent_id=comment.parent_id,
                                post_id=comment.post_id,
                                created_at=datetime.now(pytz.UTC), updated_at=datetime.now(pytz.UTC))
        db_session = LocalSession().get_session()
        try:
            db_session.add(db_comment)
            db_session.commit()
            db_session.refresh(db_comment)
            return Comment.from_orm(db_comment)
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()

    @staticmethod
    def get_comment_by_id(comment_id: uuid.UUID) -> Comment:
        db_session = LocalSession().get_session()
        try:
            db_comment = db_session.query(CommentORM).filter_by(id=comment_id).one_or_none()
            if db_comment is None:
                raise DoesNotExistException(entity_name="Comment", value=comment_id)
            return Comment.from_orm(db_comment)
        except Exception as e:
            raise e
        finally:
            db_session.close()

    @staticmethod
    def get_comments_by_user_id(user_id: uuid.UUID) -> list[Comment]:
        db_session = LocalSession().get_session()
        try:
            db_comments = db_session.query(CommentORM).filter_by(user_id=user_id).all()
            return [Comment.from_orm(comment) for comment in db_comments]
        except Exception as e:
            raise e
        finally:
            db_session.close()

    @staticmethod
    def get_comments_by_parent_id(parent_id: uuid.UUID) -> list[Comment]:
        db_session = LocalSession().get_session()
        try:
            db_comments = db_session.query(CommentORM).filter_by(parent_id=parent_id).all()
            return [Comment.from_orm(comment) for comment in db_comments]
        except Exception as e:
            raise e
        finally:
            db_session.close()

    @staticmethod
    def get_comments_by_post_id(post_id: uuid.UUID) -> list[Comment]:
        db_session = LocalSession().get_session()
        try:
            db_comments = db_session.query(CommentORM).filter_by(post_id=post_id).all()
            return [Comment.from_orm(comment) for comment in db_comments]
        except Exception as e:
            raise e
        finally:
            db_session.close()

    @staticmethod
    def update_comment(comment: Comment) -> Comment:
        db_session = LocalSession().get_session()
        try:
            db_comment = db_session.query(CommentORM).filter_by(id=comment.id).one_or_none()
            if db_comment is None:
                raise DoesNotExistException(entity_name="Comment", value=comment.id)
            db_comment.content = comment.content
            db_comment.updated_at = datetime.now(pytz.UTC)
            db_session.commit()
            db_session.refresh(db_comment)
            return Comment.from_orm(db_comment)
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()

    @staticmethod
    def delete_comment(comment_id: uuid.UUID) -> bool:
        db_session = LocalSession().get_session()
        try:
            db_comment = db_session.query(CommentORM).filter_by(id=comment_id).one_or_none()
            if db_comment is None:
                raise DoesNotExistException(entity_name="Comment", value=comment_id)
            db_session.delete(db_comment)
            db_session.commit()
            return True
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()
