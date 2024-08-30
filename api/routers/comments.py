from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, Response
from starlette import status

from api.schemas.request.comment import CommentCreateRequest, CommentUpdateRequest
from api.schemas.response.comment import CommentResponse
from core.comments.comment import Comment
from core.database.crud.comments import CommentCRUD
from core.utils.exceptions.integrity import DoesNotExistException

CommentRouter = APIRouter()


@CommentRouter.get('/comments', tags=['Comments'], response_model=List[CommentResponse])
async def get_comments(post_id: UUID):
    comments = CommentCRUD.get_comments_by_post_id(post_id=post_id)
    return comments


@CommentRouter.post('/comments', tags=['Comments'], response_model=CommentResponse)
async def create_comment(create_request: CommentCreateRequest):
    comment = CommentCRUD.create_comment(Comment(**create_request.dict()))
    return comment


@CommentRouter.put('/comments', tags=['Comments'], response_model=CommentResponse)
async def update_comment(update_request: CommentUpdateRequest):
    try:
        comment = CommentCRUD.update_comment(**update_request.dict())
        return comment
    except DoesNotExistException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'message': str(e)
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@CommentRouter.delete('/comments/{comment_id}', tags=['Comments'])
async def delete_comment(comment_id: UUID):
    try:
        if CommentCRUD.delete_comment(comment_id):
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")
    except DoesNotExistException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'message': str(e)
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
