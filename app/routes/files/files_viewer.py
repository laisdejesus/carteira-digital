from fastapi import APIRouter, Depends, File, UploadFile

from app.dependencies import token_verifier
from app.routes.files.controllers.files_controller import FilesController


router = APIRouter(
    prefix="/files", tags=["files"], dependencies=[Depends(token_verifier)]
)


@router.post("/upload")
def post_file(file: UploadFile = File(...)):
    return FilesController.post(file)


@router.get("/")
def get_files():
    return FilesController.get()
