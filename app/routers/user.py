from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession


from app.sevices.userservice import UserService
from app.schemas import UserResponse, CreateUser
from app.backend.bd_depends import get_db
from app.models import *




router = APIRouter(prefix="/users", tags=["users"])




@router.post("/create", response_model=UserResponse)
async def create_user(db: Annotated[AsyncSession, Depends(get_db)], user: CreateUser):
    await UserService.check_user(db, user)
    return await UserService.create_user(db, user)



@router.post("/token")
async def login(db: Annotated[AsyncSession, Depends(get_db)],
                form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    await UserService.get_token(db, form_data)






