from datetime import timedelta, datetime

from fastapi import HTTPException, status
from jose import jwt
from sqlalchemy import select

from app.models.user import User
from app.sevices.security import bcrypt_context
from config import settings


async def authenticate_user(db, user: str, password: str):
    user = await db.scalar(select(User).where(User.username == user))
    if not user or not bcrypt_context.verify(password, user.hashed_password) or user.is_active == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user



async def create_access_token(username: str,
                              user_id: int,
                              email: str,
                              expires_delta: timedelta):

    encode = {'sub': username, 'id': user_id, 'email': email}
    expires = datetime.now() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)