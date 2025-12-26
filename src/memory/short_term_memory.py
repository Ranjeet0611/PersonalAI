from langchain_core.runnables import RunnableWithMessageHistory
from src.constant import constant
from langchain_classic.prompts import ChatPromptTemplate,MessagesPlaceholder
class ShortTermMemory:
    store = {}
    def create_runnable_message_history(self,session_store,user_input: str,llm):
        user_prompt = ChatPromptTemplate([
            ("system", "You are a helpful AI assistant."),
            MessagesPlaceholder(variable_name="history"),
            ("human", f"{user_input}")
        ], verbose=False)
        chain = user_prompt | llm
        return RunnableWithMessageHistory(chain,get_session_history=session_store,history_messages_key=constant.CHAT_HISTORY_INPUT_KEY,input_messages_key=constant.USER_CHAT_INPUT_KEY)
