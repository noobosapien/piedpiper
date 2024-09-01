import json
import traceback
from dotenv import load_dotenv
from langchain.memory import (  # noqa
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
)
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from langchain_openai.chat_models import ChatOpenAI

from app.assistant.handlers.chat_model_start_handler import ChatModelStartHandler
from langchain.agents import AgentExecutor, create_openai_functions_agent
from app.assistant.tools.common import example_tool, date_tool
from app.assistant.tools.timeline.statement_tools import create_statement_tool
from app.assistant.tools.timeline.action_tools import create_action_tool
from app.assistant.tools.timeline.entity_tools import (
    get_entity_names_and_gid_tool,
    get_next_gid_tool,
    entity_tool,
)
from app.assistant.tools.timeline.placetimes_tools import placetimes_tool


load_dotenv()


class Assistant:
    def __init__(self):
        self.handler = ChatModelStartHandler()
        self.chat = ChatOpenAI(model="gpt-4o-mini", callbacks=[self.handler])

        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessage(
                    content=(
                        "You are an assistant who has the job of creating instances of given classes of a timeline told by a story.\n"
                        "CALL THE RELEVANT TOOLS.\n"
                        "For example when you recieve:\n"
                        "'a couple of weeks ago me and my friend at a party and then at about 11pm someone fell down the stairs and broke his neck he was probably drunk, but I think someone pushed him over'\n"
                        "You call the relevant instances using tools for this example:\n"
                        "placetimes_tool with args: place=party, place_vague=false, time=11pm, date=(calculate 2 weeks earlier from today), time_vague=true\n"
                        "get_next_gid_tool\n"
                        "entity_tool with args: gid=next_gid, name=User, main=true, multiple=false\n"
                        "get_next_gid_tool\n"
                        "entity_tool with args: gid=next_gid, name=User's friend, main=false, multiple=false\n"
                        "get_next_gid_tool\n"
                        "entity_tool with args: gid=next_gid, name=Person who fell, main=false, multiple=False\n"
                        "get_next_gid_tool\n"
                        "entity_tool with args: gid=next_gid, name=Unknown, main=false, multiple=False\n"
                        "get_entity_names_and_gid_tool\n"
                        "create_action_tool with args: order=0, by=(id of Unknown), description=Pushed somenone and he broke his neck, to=(id of Person who fell), perspective=(id of User)"
                        "create_statement_tool with args: order=1, by=(id of Unknown), description=Person who fell was drunk, perspective=(id of User), thought=true, about=(id of Person who fell), vague=false"
                    )
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )

        self.agent = create_openai_functions_agent(
            llm=self.chat,
            tools=[
                date_tool,
                get_entity_names_and_gid_tool,
                get_next_gid_tool,
                entity_tool,
                create_statement_tool,
                create_action_tool,
                placetimes_tool,
            ],
            prompt=self.prompt,
        )

        self.agent_executor = AgentExecutor(
            agent=self.agent,
            verbose=False,
            tools=[
                date_tool,
                get_entity_names_and_gid_tool,
                get_next_gid_tool,
                entity_tool,
                create_statement_tool,
                create_action_tool,
                placetimes_tool,
            ],
            memory=self.memory,
        )

    def call_assistant(self, query):
        try:
            return self.agent_executor.invoke({"input": query})
        except Exception as e:
            print(e.__traceback__)
            print(traceback.format_exc())
