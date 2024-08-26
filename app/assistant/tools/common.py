import json
from langchain.tools import Tool
from pydantic.v1 import BaseModel, Json
from typing import Annotated, Any, Optional


def get_example_for_the_output(_example_user_input):
    obj = json.dumps(
        {{"timeline": {"time": "3/1/2022", "parties": "user and the police"}}}
    )

    user_input = "On the third of january in 2022 I was with the police"

    return {"user_input": user_input, "result": obj}


class GetExampleForTheOutput(BaseModel):
    _example_user_input: Optional[str]


example_tool = Tool.from_function(
    name="get_example_for_the_output",
    description="Get an example output for the given example user input",
    func=get_example_for_the_output,
    args_schema=GetExampleForTheOutput,
)
