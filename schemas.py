from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class EventBase(BaseModel):
    title: str
    description: Optional[str]
    start_time: datetime
    end_time: datetime

class EventCreate(EventBase):
    pass

class EventOut(EventBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
