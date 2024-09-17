from datetime import timedelta, datetime

from fastapi import HTTPException, status
from jose import jwt, JWTError
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
                              expires_delta: timedelta):

    encode = {'sub': username, 'id': user_id}
    expires = datetime.now() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)



async def check_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')


        if not username or not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user"
            )

        return {
            'username': username,
            'id': user_id,

        }
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )