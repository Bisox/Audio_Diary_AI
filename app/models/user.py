from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.backend.database import Base
from app.models import *


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)


    audio_diaries = relationship('AudioDiary', back_populates='user')
    analysis_results = relationship('AnalysisResult', back_populates='user')
    recommendations = relationship('Recommendation', back_populates='user')
    activity_logs = relationship('ActivityLog', back_populates='user')
    food_diaries = relationship('FoodDiary', back_populates='user')
    day_plans = relationship('DayPlan', back_populates='user')