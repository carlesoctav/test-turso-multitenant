from fastapi import APIRouter, HTTPException

from app.api.deps import MainDBSessionDep
from app.schemas.users import User, UserBase, UserRegisterPayload
from app.core.security import get_password_hash 
from sqlmodel import insert
from app.utils import turso


router = APIRouter()


@router.post("/signup", response_model=UserBase)
def register_user(user_reg: UserRegisterPayload, session: MainDBSessionDep):
    user = User.model_validate(user_reg, update={"hashed_password": get_password_hash(user_reg.password)})
    session.add(user)
    session.commit()
    session.refresh(user)
    turso.create_database(str(user.id))
    return user

