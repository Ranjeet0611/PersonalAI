import uuid

from src.memory.short_term_memory import ShortTermMemory
from src.ollama.ollama import Ollama
from langchain_core.chat_history import InMemoryChatMessageHistory

store = {}


class ChatBot:
    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

    def get_session_id(self):
        return str(uuid.uuid4())

    def chat(self):
        try:
            ollama_model = Ollama()
            chatbot = ChatBot()
            while True:
                user_input = input("You:> ")
                if "exit" in user_input:
                    break
                llm = ollama_model.get_model()
                memory = ShortTermMemory()
                short_term_memory = memory.create_runnable_message_history(session_store=chatbot.get_session_history,
                                                                           user_input=user_input,
                                                                           llm=llm)
                config = {"configurable": {"session_id": chatbot.get_session_id()}}
                response = short_term_memory.invoke({"user_input": user_input}, config=config)
                print("ChatBot:>", response.content)
        except Exception as e:
            print(f"Error during chat: {e}")
