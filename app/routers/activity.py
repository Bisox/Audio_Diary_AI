from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.bd_depends import get_db
from app.schemas import ActivityCreate, ActivityResponse
from app.sevices.activityservice import ActivityService

router = APIRouter(prefix="/activity", tags=["activity"])


@router.get("/")
async def get_activity():
    pass



@router.post("/")
async def create_activity(db: Annotated[AsyncSession, Depends(get_db)], activity: ActivityCreate):
    await ActivityService.create_activity(db, activity)
    pass