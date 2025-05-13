from datetime import datetime, timedelta, timezone
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from jose import jwt

from app.db.models.user import User
from app.routes.users.schemas.user_schema import UserLogin
from app.settings import settings
from passlib.context import CryptContext


crypt_context = CryptContext(schemes=["sha256_crypt"])



class UserLoginController:
    """
    Classe para realizar login de usuário

    Atributos:
        db_session (Session): Sessão do banco de dados
        user_login_email (str): e-mail utilizado no login
        user_login_password (str): senha utilizado no login
    
    """
    def __init__(self, db_session: Session, user_login: UserLogin):
        self.db_session = db_session
        self.user_login_email = user_login.email
        self.user_login_password = user_login.password

    def verify_user_password(self, user_password):
        return crypt_context.verify(self.user_login_password, user_password)

    def post(self, expires_in: int = 30):
        """Método para realizar login"""

        user_exist = User.get_user_by_email(
            self.db_session, self.user_login_email
        )

        if not user_exist:
            raise HTTPException(
                status_code=400, detail="Invalid email or password"
            )

        match_password = self.verify_user_password(
            user_exist.hashed_password,
        )
        if not match_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        exp = datetime.now(timezone.utc) + timedelta(minutes=expires_in)

        payload = {"sub": self.user_login_email, "exp": exp}

        access_token = jwt.decode(
                payload,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )

        return {
            "access_token": access_token,
            "expires": exp.isoformat(),
        }
