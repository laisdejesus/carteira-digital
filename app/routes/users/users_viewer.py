from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.routes.users.controllers.user_controller import UserController
from app.routes.users.controllers.user_login_controller import (
    UserLoginController
)
from app.routes.users.schemas.user_schema import (
    UserCreate, UserLogin, UserSchema
)

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/register", response_model=UserSchema)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserController(user.email, db).post(user)


@router.post("/login")
def user_login(
    request_form_user: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user_login = UserLogin(
        email=request_form_user.username, password=request_form_user.password
    )
    return UserLoginController(db, user_login).post()
