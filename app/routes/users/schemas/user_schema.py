from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    email: str
    name: str
    document_number: str


class UserSchema(UserBase):
    id: int
    is_active: bool


class UserLogin(UserBase):
    password: str
