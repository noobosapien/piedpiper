from app.assistant.classes.engine import get_engine
from langchain.tools import StructuredTool
from app.assistant.classes.placetime import Placetime
from pydantic.v1 import BaseModel, Field
from typing import Optional

engine = get_engine()


def create_place_time(place="", place_vague=True, time="", date="", time_vague=True):
    timeline = engine.getTimeline(0)
    timeline.addPlacetime(Placetime())

    pt1: Placetime = timeline.getPlacetime(0)
    pt1.createPlace(place, place_vague)
    pt1.createTime(time, date, time_vague)

    return True


class CreatePlaceTime(BaseModel):
    place: str = Field(description="place name")
    place_vague: bool = Field(
        description="whether the place is vague determined by whethe the given place has a name or a general description"
    )
    time: Optional[str] = Field(
        description="time of the event only of given otherwise nothing"
    )
    date: str = Field(
        description="date as described could be specific if it can be calculated or general if it cannot be calculated"
    )
    time_vague: bool = Field(
        description="whether the date is vague depending on whether the date can be calculated if it can be calculated it is not vague"
    )


placetimes_tool = StructuredTool.from_function(
    name="create_place_time",
    description="Create an instance of class Placetime which holds only the information of the time and the place of the event",
    func=create_place_time,
    args_schema=CreatePlaceTime,
)
