from langchain_classic.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.memory.chat_message_histories import SQLChatMessageHistory

memory = None


class LongTermMemory:

    def __init__(self):
        self.memory_type = "long-term"
        self.memory = None

    def save_memory(self, user_input, output):
        global memory
        memory.save_context({"input": user_input},
                            {"output": output})

    def get_memory(self, user_input: str, session_id: str, llm):
        try:
            prompt_template = ChatPromptTemplate(
                [("system", "You are a helpful AI assistant."), MessagesPlaceholder(variable_name="history"),
                 ("human", f"{user_input}")])
            global memory
            memory = ConversationBufferMemory(chat_memory=SQLChatMessageHistory(
                connection_string="postgresql+psycopg2://postgres:root@localhost:5432/postgres",
                session_id=session_id), return_messages=True)
            chain = (RunnablePassthrough.assign(history=lambda x: memory.chat_memory.messages)
                     | prompt_template | llm)
            return chain
        except Exception as e:
            print(f"Failed to initialize long term memory: {e}")
            return None

    def get_history(self):
        try:
            global memory
            return memory.chat_memory.messages
        except Exception as e:
            print(f"Failed to get history: {e}")
            return None
