from fastapi import Depends
from typing import Annotated
from sqlmodel import Session, create_engine 
from app.core.db import main_engine
from app.schemas.users import User
from app.utils import turso

def main_get_session():
    with Session(main_engine) as session:
        yield session

MainDBSessionDep = Annotated[Session, Depends(main_get_session)]



#TODO: need to fix this
def user_get_session(user: User):
    connect_args = {"check_same_thread": False}
    user_engine = create_engine(turso.get(str(user.id)), connect_args=connect_args)
    with Session(user_engine) as session:
        yield session


UserDBSessionDep = Annotated[Session, Depends(user_get_session)]

