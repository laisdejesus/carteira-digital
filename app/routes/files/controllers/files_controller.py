import os

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

from app.db.models.user import User

# from app.users.schemas.user_schema import UserCreate


class FilesController:
    """Classe para realizar Gestão do documentos"""

    def post(file):
        """Método para fazer upload de arquivos"""
        with open(f"uploads/{file.filename}", "wb") as f:
            f.write(file.file.read())
        return {"message": f"File '{file.filename} saved successfully"}

    def get():
        """Método para fazer consultar arquivos"""
        files = [
            file
            for file in os.listdir("uploads")
            if os.path.isfile(os.path.join("uploads", file))
        ]
        return files
