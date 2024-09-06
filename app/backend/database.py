from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = AsyncSession(engine, class_=AsyncEngine)


class Base(DeclarativeBase):
    pass