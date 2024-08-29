from pydantic import BaseModel

from typing import Any
from pydantic import Json


class TestBase(BaseModel):
    pass


class TestReturn(TestBase):
    story: Json[Any]
