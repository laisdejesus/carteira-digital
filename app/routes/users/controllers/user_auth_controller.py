from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.db.models.user import User
from app.settings import settings

from passlib.context import CryptContext


crypt_context = CryptContext(schemes=["sha256_crypt"])


class UserAuthController:
    """
    Classe para realizar gestão de autenticação de usuário

    Atributos:
        db_session (Session): Sessão do banco de dados
    """
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_user_token(self, access_token):
        """Método para buscar usuário do token relacionado"""
        try:
            data = jwt.decode(
                access_token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )
            user = User.get_user_by_email(self.db_session, email=data["sub"])

        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        return user

    def verify_token(self, access_token):
        """Método para verificar token do usuário"""
        try:
            self.get_user_token(access_token)
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")
