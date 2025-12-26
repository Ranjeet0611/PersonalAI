from langchain_community.chat_models import ChatOllama
from src.constant import constant
class Ollama:
    def get_model(self):
        try:
            llm = ChatOllama(model = constant.OLLAMA_MODEL_NAME,temperature=0,verbose=False)
            return llm
        except Exception as e:
            print(f"Error initializing Ollama LLM: {e}")
            return None
