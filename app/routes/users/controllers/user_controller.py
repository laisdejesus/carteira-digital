from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.db.models.user import User


class UserController:
    """
    Classe para realizar registro de usuário

    Atributos:
        db_session (Session): Sessão do banco de dados
    """
    def __init__(self, email, db_session: Session): 
        self.email = email
        self.db_session = db_session

    def post(self, user):
        """Método para realizar cadastro de usuário"""
        user_exist = User.get_user_by_email(self.db_session, self.email)
        if user_exist:
            raise HTTPException(
                tatus_code=400, detail="User email already registered"
            )
        return User.create_user(
            self.db_session, user=user
        )
