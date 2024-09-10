from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.backend.database import Base
from app.models import *


class AnalysisResult(Base):
    __tablename__ = 'analysis_results'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    audio_diary_id = Column(Integer, ForeignKey('audio_diaries.id'))
    mood = Column(String)                                  # Определение настроения (радость, грусть, тревога и т.д.)
    stress_level = Column(Integer)                         # Уровень стресса
    key_insights = Column(Text)                            # Ключевые выводы из анализа

    created_at = Column(DateTime, default = lambda: datetime.now(timezone.utc).replace(tzinfo=None))

    # Связи
    user = relationship('User', back_populates='analysis_results')
    audio_diary = relationship('AudioDiary', back_populates='analysis_result')
