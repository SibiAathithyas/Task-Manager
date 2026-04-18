from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True