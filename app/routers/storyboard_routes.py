import logging


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.storyboard_schema import StoryboardReturn, StoryboardCreate
from app.assistant.agent import Assistant

router = APIRouter()
logger = logging.getLogger("app")
assistant = Assistant()


@router.post("/", response_model=StoryboardReturn, status_code=201)
def storyboard(data: StoryboardCreate):
    try:
        return assistant.call_assistant(data.model_dump_json())

    except HTTPException as http_exc:
        logger.error(f"Error while retrieving storyboard: {http_exc}")
        raise

    except Exception as e:
        logger.error(f"Unexpected error while creating storyboard: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
