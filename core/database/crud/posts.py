from core.database.crud.base import CRUDModel
from datetime import datetime
from uuid import uuid4, UUID

import pytz

from core.database.connection import LocalSession
from core.posts.models.post import PostORM
from core.posts.post import Post
from core.utils.exceptions.integrity import DoesNotExistException


class PostCRUD(CRUDModel):

    @staticmethod
    def create_post(post: Post):
        post_id = uuid4()
        db_post = PostORM(id=post_id, user_id=post.user_id, content=post.content, title=post.title,
                          created_at=datetime.now(pytz.UTC),
                          updated_at=datetime.now(pytz.UTC))
        db_session = LocalSession().get_session()
        try:
            db_session.add(db_post)
            db_session.commit()
            db_session.refresh(db_post)
            return Post.from_orm(db_post)
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()

    @staticmethod
    def get_post(post_id: UUID):
        db_session = LocalSession().get_session()
        try:
            db_post = db_session.query(PostORM).filter_by(id=post_id).one_or_none()
            if db_post is None:
                raise DoesNotExistException(entity_name="Post", value=post_id)
            return Post.from_orm(db_post)
        except Exception as e:
            raise e
        finally:
            db_session.close()

    @staticmethod
    def get_all_posts(user_id: UUID):
        db_session = LocalSession().get_session()
        try:
            db_posts = db_session.query(PostORM).filter_by(user_id=user_id).all()
            return [Post.from_orm(post) for post in db_posts]
        except Exception as e:
            raise e
        finally:
            db_session.close()

    @staticmethod
    def update_post(post: Post):
        db_session = LocalSession().get_session()
        try:
            db_post = db_session.query(PostORM).filter_by(id=post.id).one_or_none()
            if db_post is None:
                raise DoesNotExistException(entity_name="Post", value=post.id)
            db_post.content = post.content
            db_post.title = post.title
            db_post.updated_at = datetime.now(pytz.UTC)
            db_session.commit()
            db_session.refresh(db_post)
            return Post.from_orm(db_post)
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()

    @staticmethod
    def delete_post(post_id: UUID) -> bool:
        db_session = LocalSession().get_session()
        try:
            db_post = db_session.query(PostORM).filter_by(id=post_id).one_or_none()
            if db_post is None:
                raise DoesNotExistException(entity_name="Post", value=post_id)
            db_session.delete(db_post)
            db_session.commit()
            return True
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()
