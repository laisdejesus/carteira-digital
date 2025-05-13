from fastapi import FastAPI

from app.routes.credit import credit_viewer
from app.routes.files import files_viewer
from app.routes.users import users_viewer


app = FastAPI()


@app.get("/health")
def health_check():
    return "ok, its health"


app.include_router(users_viewer.router)
app.include_router(files_viewer.router)
app.include_router(credit_viewer.router)
