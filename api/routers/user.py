from uuid import UUID

from fastapi import APIRouter, HTTPException
from starlette import status

from api.schemas.request.comment import CommentCreateRequest
from api.schemas.request.user import UserCreateRequest
from api.schemas.response.user import UserResponse
from core.database.crud.user import UserCRUD
from core.users.user import User
from core.utils.exceptions.integrity import DoesNotExistException, AlreadyExistsException

UserRouter = APIRouter()


@UserRouter.get('/user/{username}', tags=['User'], response_model=UserResponse)
async def get_user(username: str):
    try:
        user = UserCRUD.get_user(username)
        return user
    except DoesNotExistException as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'message': str(e)
        })
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


@UserRouter.post('/user', tags=['User'], response_model=UserResponse)
async def create_user(create_request: UserCreateRequest):
    try:
        user = UserCRUD.create_user(user=User(username=create_request.username))
        return user
    except AlreadyExistsException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
            "message": str(e)
        })
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")
