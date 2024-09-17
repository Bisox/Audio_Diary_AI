from sqlalchemy import select, insert
from typing import Annotated

from app.models import ActivityLog


class ActivityService:


    @staticmethod
    async def create_activity(db, activity):
        create_activity_query = insert(ActivityLog).values(activity_type=activity.activity_type,
                                                           duration=activity.duration)
        pass