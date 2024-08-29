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

load_dotenv()


class Assistant:
    def __init__(self):
        self.handler = ChatModelStartHandler()
        self.chat = ChatOpenAI(model="gpt-4o", callbacks=[self.handler])
        self.example1 = json.dumps(
            {"timeline": {"time": "A few weeks back", "parties": "user and friend"}}
        )
        self.example2 = json.dumps(
            {"timeline": {"time": "March", "parties": "alex and naomi"}}
        )

        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessage(
                    content=(
                        "You are an assistant who has the job of creating a JSON representation of a timeline told by a story.\n"
                        "For example when you recieve:\n"
                        "'a couple of weeks ago me and my friend'\n"
                        "You make a json representation with the important information of the sentence and send back something like:\n"
                        f"{self.example1}\n"
                        "Another example, when you recieve:\n"
                        "'5 months back alex and naomi'\n"
                        "If the date or time can be deduced from the input\n"
                        "The output should be like:\n"
                        f"{self.example2}\n"
                        "IMPORTANT: ONLY TRY TO EXTRACT THE IMPORATANT INFORMATION FOR THE JSON OBJECT, USE THE 'date_tool' FUNCTION AND CREATE THE OUTPUT IN A DATE FORMAT\n"
                        "IMPORTANT: YOUR OUTPUT MUST ONLY CONTAIN JSON"
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
            tools=[example_tool, date_tool],
            prompt=self.prompt,
        )

        self.agent_executor = AgentExecutor(
            agent=self.agent,
            verbose=False,
            tools=[example_tool, date_tool],
            memory=self.memory,
        )

    def call_assistant(self, query):
        try:
            return self.agent_executor.invoke({"input": query})
        except Exception as e:
            print(e.__traceback__)
            print(traceback.format_exc())
