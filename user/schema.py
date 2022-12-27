from typing import Optional
from pydantic import BaseModel, validator, EmailStr


class User(BaseModel):
    username: str


class UserCreate(User):
    password: str
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserInDB(User):
    hashed_password: str
