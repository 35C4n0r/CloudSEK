from datetime import datetime
from uuid import uuid4

import pytz
from sqlalchemy.exc import IntegrityError

from core.database.connection import LocalSession
from core.database.crud.base import CRUDModel
from core.users.models.user import UserORM
from core.users.user import User
from core.utils.exceptions.integrity import DoesNotExistException, AlreadyExistsException


class UserCRUD(CRUDModel):

    @staticmethod
    def create_user(user: User) -> User:
        user_id = uuid4()
        db_user = UserORM(id=user_id, username=user.username,
                          created_at=datetime.now(pytz.UTC), updated_at=datetime.now(pytz.UTC))
        db_session = LocalSession().get_session()
        db_session.add(db_user)
        try:
            db_session.commit()
            db_session.refresh(db_user)
            user_obj = User.from_orm(db_user)
            return user_obj
        except IntegrityError as e:
            raise AlreadyExistsException(entity_name="User", name=user.username)
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()

    @staticmethod
    def get_user(username: str) -> User:
        db_session = LocalSession().get_session()
        try:
            db_user = db_session.query(UserORM).filter_by(username=username).one_or_none()
            if db_user is None:
                raise DoesNotExistException(entity_name="User", value=username)
            return User.from_orm(db_user)
        except Exception as e:
            raise e
        finally:
            db_session.close()
