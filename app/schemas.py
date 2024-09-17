from datetime import datetime

from pydantic import BaseModel



class CreateUser(BaseModel):
    username: str
    email: str
    hashed_password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True



class ActivityCreate(BaseModel):
    activity_type: str
    duration: int


class ActivityResponse(BaseModel):
    id: int
    activity_type: str
    duration: int
    created_at: datetime


    class Config:
        from_attributes = True