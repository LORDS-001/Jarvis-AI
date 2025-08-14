# app/schemas.py
from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    to: EmailStr
    subject: str | None = None
    content: str

class RememberRequest(BaseModel):
    note: str

class SearchRequest(BaseModel):
    query: str
