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
    user_id: int
    activity_type: str
    duration: int


class ActivityResponse(BaseModel):
    activity_id: int
    duration: int

    class Config:
        from_attributes = True