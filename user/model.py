from pydantic import BaseModel, validator, EmailStr


class User(BaseModel):
    name: str
    username: str
    email: EmailStr
    height: float | None = None
    weight: float | None = None

    @validator('name')
    def check_names_not_empty(cls, v):
        assert v != '', 'Name field is required.'
        return v

    @validator('username')
    def check_username_not_empty(cls, v):
        assert v != '', 'Username field is required.'
        return v
