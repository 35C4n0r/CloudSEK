from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    username: str
