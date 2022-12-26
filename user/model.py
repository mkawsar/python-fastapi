from pydantic import BaseModel, ValidationError, validator


class User(BaseModel):
    name: str
    email: str
    height: float | None = None
    weight: float | None = None

    @validator('name')
    def check_names_not_empty(cls, v):
        assert v != '', 'Empty strings are not allowed.'
        return v
