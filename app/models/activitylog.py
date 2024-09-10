from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.backend.database import Base
from app.models import *


class ActivityLog(Base):
    __tablename__ = 'activity_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    activity_type = Column(String)                    # Тип активности (работа, учеба, отдых)
    duration = Column(Integer)                        # Продолжительность в минутах
    created_at = Column(DateTime, default = lambda: datetime.now(timezone.utc).replace(tzinfo=None))

    # Связь с пользователем
    user = relationship('User', back_populates='activity_logs')