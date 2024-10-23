import uuid
from fastapi.routing import BaseModel
from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
    username: str


class User(UserBase, table = True):
    id: uuid.UUID = Field(default_factory= uuid.uuid4, primary_key= True)
    hashed_password: str


class UserRegisterPayload(SQLModel):
    username: str
    password: str
