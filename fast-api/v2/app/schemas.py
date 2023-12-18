from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
"""SCHEMAs"""
"""treat them as request/response"""

# SQLAlchemy style and Pydantic style
# https://fastapi.tiangolo.com/tutorial/sql-databases/#sqlalchemy-style-and-pydantic-style

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        """We need pydantic to convert it to a regular pydantic"""
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    # title: str
    # content: str
    # published: bool
    created_at: datetime
    owner_id: int
    owner: UserOut # return pydantic model

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
