import logging
import json
import re

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.assistant.classes.engine import get_engine
from app.schemas.storyboard_schema import StoryboardReturn, StoryboardCreate
from app.assistant.agent import Assistant

router = APIRouter()
logger = logging.getLogger("app")
assistant = Assistant()

engine = get_engine()


@router.post("/", response_model=StoryboardReturn, status_code=201)
def storyboard(data: StoryboardCreate):
    try:
        engine.clear()
        engine.createTimeline()

        assistant.call_assistant(data.model_dump_json())
        message = json.dumps(engine.getTimeline(0).serialize())

        return StoryboardReturn(story=message)

    except HTTPException as http_exc:
        logger.error(f"Error while retrieving storyboard: {http_exc}")
        raise

    except Exception as e:
        logger.error(f"Unexpected error while creating storyboard: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
