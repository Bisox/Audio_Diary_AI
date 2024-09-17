from datetime import timedelta

from fastapi import HTTPException, Depends

from sqlalchemy import select, insert
from typing import Annotated

from app.sevices.auth_helpers import authenticate_user, create_access_token, check_token
from app.sevices.security import bcrypt_context, oauth2_scheme
from app.models import User




class UserService:


    @staticmethod
    async def check_user(db, user):
        check_query = select(User).where(User.email == user.email)
        result = await db.execute(check_query)
        existing_user = result.scalar_one_or_none()

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")



    @staticmethod
    async def create_user(db, user):
        create_user_query = insert(User).values(username=user.username,
                                                email=user.email,
                                                hashed_password=bcrypt_context.hash(user.hashed_password)
                                                ).returning(User.id, User.username, User.email, User.is_active)

        result = await db.execute(create_user_query)
        new_user = result.fetchone()
        await db.commit()

        if new_user is None:
            raise HTTPException(status_code=404, detail="User not found after creation")
        return new_user



    @staticmethod
    async def get_token(db, user):
          user_auth = await authenticate_user(db, user.username, user.password)
          token = await create_access_token(user_auth.username,
                                            user_auth.id,
                                            expires_delta=timedelta(minutes=20))

          return {
              "access_token": token,
              "token_type": "bearer"
          }


    @staticmethod
    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        user_data = await check_token(token)
        return user_data


