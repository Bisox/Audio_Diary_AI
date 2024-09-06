from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.backend.database import Base
from app.models import *


class AudioDiary(Base):
    __tablename__ = 'audio_diaries'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    audio_file_url = Column(String, nullable=False)                  # Ссылка на аудиофайл
    transcript = Column(Text)                                        # Текстовая версия аудио
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Связь с пользователем
    user = relationship('User', back_populates='audio_diaries')
    analysis_result = relationship('AnalysisResult', back_populates='audio_diary', uselist=False)