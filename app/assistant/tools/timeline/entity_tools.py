from app.assistant.classes.engine import get_engine
from langchain.tools import StructuredTool
from app.assistant.classes.placetime import Placetime
from app.assistant.classes.entity import Entity
from pydantic.v1 import BaseModel, Field
from typing import Optional

engine = get_engine()


def get_entity_names_and_gid():
    timeline = engine.getTimeline(0)
    pt1: Placetime = timeline.getPlacetime(0)

    entities = []

    if pt1.entities:
        for entity in pt1.entities:
            entities.append(
                {
                    "gid": entity.gid,
                    "name": entity.name,
                }
            )

    return entities


get_entity_names_and_gid_tool = StructuredTool.from_function(
    name="get_entity_names_and_gid",
    description="Get the list of entities in the timeline and their gid",
    func=get_entity_names_and_gid,
)


def get_next_gid():
    timeline = engine.getTimeline(0)
    pt1: Placetime = timeline.getPlacetime(0)

    if pt1 and pt1.entities:
        return len(pt1.entities)
    else:
        return 0


get_next_gid_tool = StructuredTool.from_function(
    name="get_next_gid",
    description="Get the next gid of the new entity to create",
    func=get_next_gid,
)


def create_entity(gid, name, main=False, multiple=False):
    timeline = engine.getTimeline(0)
    timeline.addPlacetime(Placetime())

    pt1: Placetime = timeline.getPlacetime(0)

    entity = Entity(gid, name, main, multiple)
    pt1.addEntity(entity)


class CreateEntity(BaseModel):
    gid: int = Field(description="the new id of the entity")
    name: str = Field(description="name of the new entity")
    main: Optional[bool] = Field(
        description="is the story told with the perspective of this entity"
    )
    multiple: Optional[bool] = Field(
        description="is it a single entity or multiple entities depends on the name and the description"
    )


entity_tool = StructuredTool.from_function(
    name="create_entity",
    description="Create an instance of class Entity which holds only the information of the entity",
    func=create_entity,
    args_schema=CreateEntity,
)
