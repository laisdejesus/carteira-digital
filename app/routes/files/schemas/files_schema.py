import re

from pydantic import BaseModel, field_validator


class FileUpload(BaseModel):
    type_document: str


class FileResponse(BaseModel):
    id: int
    is_active: bool


class GetFileResponse(BaseModel):
    files: list


class GetFiles(BaseModel):
    file: list
