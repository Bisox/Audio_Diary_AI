from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.backend.database import Base
from app.models import *


class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recommendation_text = Column(Text)                   # Текст рекомендации
    type = Column(String)                                # Тип рекомендации (психологическая, физическая, по питанию)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


    user = relationship('User', back_populates='recommendations')