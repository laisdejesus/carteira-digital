from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.models.user import User
from app.db.models.credit_user import CreditUser


class CreditUserController:
    """
    Classe para realizar Gestão do transporte público

    Atributos:
        db_session (Session): Sessão do banco de dados
        user_id (int):Identificador do usuário
    """
    def __init__(self, db_session: Session, user: User):
        self.db_session = db_session
        self.user_id = user.id

    def get(self):
        """Método de consulta de saldo do passe de transporte público"""

        credit = CreditUser.get_credit_by_user_id(
            self.db_session, self.user_id
        )
        if not credit:
            credit = 0.0
        return JSONResponse(
            status_code=200, content={"message": f"Credit value is R${credit}"}
        )

    def put(self, amount: float):
        """
        Método para recarga do passede transporte público

        Atributos:
            amount (float): Valor da recarga
        """

        current_credit = CreditUser.get_credit_by_user_id(
            self.db_session, self.user_id
        )
        if not current_credit:
            credit = CreditUser.create_credit(
                self.db_session, self.user_id, amount
            )
            return JSONResponse(
                status_code=200, content={
                    "message": f"Credit valueeeee is R${credit}"
                }
            )

        new_credit = current_credit.credit_value + amount

        credit = CreditUser.update_credit(
            self.db_session, self.user_id, new_credit
        )
        return JSONResponse(
            status_code=200,
            content={"message": f"Credit value is R${credit.credit_value}"},
        )
