from api.routers.comments import CommentRouter

from typing import List

from api.routers.posts import PostsRouter
from api.routers.user import UserRouter

ROUTES: List[dict] = [
    {"router": CommentRouter},
    {"router": PostsRouter},
    {"router": UserRouter}
]
