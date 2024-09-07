from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.backend.database import Base
from app.models import *


class FoodDiary(Base):
    __tablename__ = 'food_diaries'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    meal_time = Column(String)                          # Время приема пищи (завтрак, обед, ужин)
    food_description = Column(Text)                     # Описание еды
    created_at = Column(DateTime, default=lambda: datetime.now().replace(tzinfo=None))


    user = relationship('User', back_populates='food_diaries')