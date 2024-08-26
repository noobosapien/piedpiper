from pydantic import BaseModel, StringConstraints
from typing import Annotated, Optional

from typing import List, Any
from pydantic import Json


class StoryboardBase(BaseModel):
    pass


class StoryboardCreate(StoryboardBase):
    words: Annotated[str, StringConstraints(min_length=1)]


class StoryboardReturn(StoryboardBase):
    story: Json[Any]
