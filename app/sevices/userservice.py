from fastapi import HTTPException

from sqlalchemy import select, insert

from app.sevices.security import bcrypt_context
from app.models import User




class UserService:


    @staticmethod
    async def check_user(db, user):
        check_query = select(User).where(User.email == user.email)
        result = await db.execute(check_query)
        existing_user = result.scalars().fetchall()

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


