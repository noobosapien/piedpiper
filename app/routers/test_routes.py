import logging
import json

from fastapi import APIRouter, HTTPException

from app.schemas.test_schema import TestReturn
from app.assistant.classes.engine import get_engine
from app.assistant.classes.placetime import Placetime
from app.assistant.classes.entity import Entity
from app.assistant.classes.statement import Statement
from app.assistant.classes.action import Action

router = APIRouter()
logger = logging.getLogger("app")


@router.post("/test", response_model=TestReturn, status_code=201)
def test_path():
    try:
        engine = get_engine()
        engine.createTimeline()

        timeline = engine.getTimeline(0)
        timeline.addPlacetime(Placetime())

        pt1: Placetime = timeline.getPlacetime(0)
        pt1.createPlace("Festival", False)
        pt1.createTime(None, "Couple of weeks ago", True)

        emma = Entity(0, "Emma", True)
        bf = Entity(1, "Boyfriend")
        police = Entity(2, "Police", multiple=True)

        pt1.addEntity(emma)
        pt1.addEntity(bf)
        pt1.addEntity(police)

        statement1 = Statement(
            emma, "Knew she didn't have anything", emma, True, about=emma, vague=False
        )
        statement1.setOrder(0)
        pt1.addStatement(statement=statement1)

        action1 = Action(
            bf, "Placed drugs in the jacket after seeing the dogs", emma, emma
        )
        action1.setOrder(1)
        pt1.addAction(action1)

        action2 = Action(police, "Dogs sniffed drugs", emma, emma)
        action2.setOrder(2)
        pt1.addAction(action2)

        action3 = Action(police, "Found drugs in the jacket", emma, emma)
        action3.setOrder(3)
        pt1.addAction(action3)

        statement2 = Statement(
            emma, "She had no idea where it came from", emma, False, emma, False
        )
        statement2.setOrder(4)
        pt1.addStatement(statement2)

        statement3 = Statement(
            police, "Thinks she is being evasive", emma, True, emma, False
        )
        statement3.setOrder(5)
        pt1.addStatement(statement3)

        timeline_dict = timeline.serialize()

        return TestReturn(story=json.dumps(timeline_dict))

    except HTTPException as http_exc:
        logger.error(f"Error while retrieving storyboard: {http_exc}")
        raise

    except Exception as e:
        logger.error(f"Unexpected error while creating storyboard: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
