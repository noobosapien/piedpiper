from app.assistant.classes.engine import get_engine
from langchain.tools import StructuredTool
from app.assistant.classes.placetime import Placetime
from app.assistant.classes.action import Action
from app.assistant.classes.entity import Entity
from pydantic.v1 import BaseModel, Field
from typing import Optional

engine = get_engine()


def create_action(order, by, description, to, perspective):
    placetime = engine.getTimeline(0).getPlacetime(0)
    action = Action(order, by, description, to, perspective)
    placetime.addAction(action)

    return True


class CreateAction(BaseModel):
    order: int = Field(
        description="the order of this action depending on the story and other actions and statements"
    )
    by: int = Field(
        description="the gid of the entity who did this action use the get_entity_names_and_gid_tool and find the gid of the entity to put here"
    )
    description: str = Field(description="A short description of the action performed")
    to: int = Field(
        description="the gid of the entity who was at the recieving end of this action use the get_entity_names_and_gid_tool and find the gid of the entity to put here"
    )
    perspective: int = Field(
        description="the gid of the entity who says about the action, use the get_entity_names_and_gid_tool and find the gid of the entity to put here"
    )


create_action_tool = StructuredTool.from_function(
    name="create_action",
    description="Create an instance of class action which holds only the information of the action done by the entity",
    func=create_action,
    args_schema=CreateAction,
)
