from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.backend.database import Base
from app.models import *


class DayPlan(Base):
    __tablename__ = 'day_plans'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    plan_description = Column(Text)                         # Описание плана дня
    productivity_score = Column(Integer)                    # Оценка продуктивности (0-100)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


    user = relationship('User', back_populates='day_plans')