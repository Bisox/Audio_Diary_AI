from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from app.schemas import UserResponse, CreateUser
from app.backend.bd_depends import get_db
from app.models import *

from passlib.context import CryptContext


router = APIRouter(prefix="/users", tags=["users"])

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.post("/create", response_model=UserResponse)
async def create_user(db: Annotated[AsyncSession, Depends(get_db)], user: CreateUser):
    create_user_query = insert(User).values(username=user.username,
                                            email=user.email,
                                            hashed_password = bcrypt_context.hash(user.hashed_password)
                                            ).returning(User.id, User.username, User.email, User.is_active)

    result = await db.execute(create_user_query)
    new_user = result.fetchone()

    await db.commit()

    if new_user is None:
        raise HTTPException(status_code=404, detail="User not found after creation")


    return new_user





