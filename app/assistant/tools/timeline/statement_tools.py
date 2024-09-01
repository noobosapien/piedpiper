from app.assistant.classes.engine import get_engine
from langchain.tools import StructuredTool
from app.assistant.classes.statement import Statement
from pydantic.v1 import BaseModel, Field

engine = get_engine()


def create_statement(order, by, description, perspective, thought, about, vague):
    placetime = engine.getTimeline(0).getPlacetime(0)
    statement = Statement(order, by, description, perspective, thought, about, vague)
    placetime.addStatement(statement)

    return True


class CreateStatement(BaseModel):
    order: int = Field(
        description="the order of this statement depending on the story and other actions and statements"
    )
    by: int = Field(
        description="the gid of the entity who is the primary entity of this statement, use the get_entity_names_and_gid_tool and find the gid of the entity to put here"
    )
    description: str = Field(description="A short description of this statement")
    perspective: int = Field(
        description="the gid of the entity who says this statement, use the get_entity_names_and_gid_tool and find the gid of the entity to put here"
    )
    thought: bool = Field(description="Is this statement a matter of fact or not ")
    about: int = Field(description="the secondary entity of this statement")
    vague: bool = Field(
        description="is this a vague statement or not depending on whether the perspective character thinks about it or it has actully happened"
    )


create_statement_tool = StructuredTool.from_function(
    name="create_statement",
    description="Create an instance of class statement which holds only the information of the statement by the entity",
    func=create_statement,
    args_schema=CreateStatement,
)
