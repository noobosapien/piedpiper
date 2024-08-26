import json
from langchain.tools import Tool, StructuredTool
from pydantic.v1 import BaseModel, Json
from typing import Annotated, Any, Optional
from datetime import datetime


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


def get_current_date(_input=""):
    return {"date": str(datetime.today().strftime("%d-%m-%Y"))}


class GetCurrentDate(BaseModel):
    _input: Optional[str]


date_tool = StructuredTool.from_function(
    name="get_current_date",
    description="Gettodays's date in the format day-month-year",
    func=get_current_date,
    args_schema=GetCurrentDate,
)
