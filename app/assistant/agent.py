import json
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
from app.assistant.tools.common import example_tool

load_dotenv()


class Assistant:
    def __init__(self):
        self.handler = ChatModelStartHandler()
        self.chat = ChatOpenAI(model="gpt-4o", callbacks=[self.handler])
        self.example = json.dumps(
            {"timeline": {"time": "A few weeks back", "parties": "user and friend"}}
        )
        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessage(
                    content=(
                        "You are an assistant who has the job of creating a JSON representation of a timeline told by a story.\n"
                        "For example when you recieve:\n"
                        "'a couple of weeks ago me and my friend'\n"
                        "You make a json representation with the important information of the sentence and send back something like:\n"
                        f"{self.example}\n"
                        "IMPORTANT: ONLY TRY TO EXTRACT THE IMPORATANT INFORMATION FOR THE JSON OBJECT\n"
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
            tools=[example_tool],
            prompt=self.prompt,
        )

        self.agent_executor = AgentExecutor(
            agent=self.agent,
            verbose=False,
            tools=[example_tool],
            memory=self.memory,
        )

    def call_assistant(self, query):
        story = {"timeline": {"A few weeks back": {}}}

        try:
            res = self.agent_executor.invoke({"input": query})
            print(res)
        except Exception as e:
            print(e.__traceback__)

        return {"story": json.dumps(story)}
