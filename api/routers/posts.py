from uuid import UUID

from fastapi import Request, APIRouter, Response, HTTPException
from starlette import status
from fastapi.responses import JSONResponse

from api.schemas.request.post import PostCreateRequest, PostUpdateRequest
from api.schemas.response.post import PostResponse
from core.database.crud.posts import PostCRUD
from core.posts.post import Post
from core.utils.exceptions.integrity import DoesNotExistException

PostsRouter = APIRouter()


@PostsRouter.get("/posts/{post_id}", tags=["Posts"], response_model=PostResponse)
async def get_post(post_id: UUID):
    try:
        post = PostCRUD.get_post(post_id)
        return post
    except DoesNotExistException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'message': str(e)
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


@PostsRouter.post("/posts", tags=["Posts"], response_model=PostResponse)
async def create_post(create_request: PostCreateRequest):
    post = PostCRUD.create_post(Post(**create_request.dict()))
    return post


@PostsRouter.put("/posts", tags=["Posts"], response_model=PostResponse)
async def update_post(update_post_request: PostUpdateRequest):
    try:
        post = PostCRUD.update_post(Post(**update_post_request.dict()))
        return post
    except DoesNotExistException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'message': str(e)
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


@PostsRouter.delete("/posts/{post_id}", tags=["Posts"])
async def delete_post(post_id: UUID):
    try:
        post = PostCRUD.delete_post(post_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except DoesNotExistException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'message': str(e)
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")
