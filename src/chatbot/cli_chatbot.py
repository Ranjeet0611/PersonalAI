import uuid

from src.memory.long_term_memory import LongTermMemory
from src.memory.memory_decider import MemoryDecider
from src.memory.short_term_memory import ShortTermMemory
from langchain_core.prompts import PromptTemplate
from src.models.ollama import Ollama
import asyncio

def get_session_id():
    return str(uuid.uuid4())


def get_history_messages(self, long_term_history, short_term_history):
    short_term_history_text = "\n".join(
        f"{m['role']}: {m['content']}" for m in short_term_history
    )
    long_term_history_text = "\n".join(
        f"{m['role']}: {m['content']}" for m in long_term_history
    )
    short_term_history_text += "\n" + long_term_history_text
    return short_term_history_text


class CLIChatbot:
    def __init__(self):
        self.type = "cli"

    def cli_chat(self):
        try:
            ollama_model = Ollama()
            session_id = get_session_id()
            short_term_memory = ShortTermMemory()
            long_term_memory = LongTermMemory()
            memory_decider = MemoryDecider()
            while True:
                user_input = input("You:> ")
                if "exit" in user_input:
                    short_term_memory.clear_short_term_memory(session_id=session_id)
                    break
                llm = ollama_model.get_model()
                short_term_history = short_term_memory.get_short_term_memory(session_id)
                long_term_history = long_term_memory.search_long_term(user_input, limit=3)
                if short_term_history or long_term_history:
                    short_term_history_text = get_history_messages(long_term_history, short_term_history)
                else:
                    short_term_history_text = ""

                prompt = PromptTemplate(
                    input_variables=["user_input", "short_term_history"],
                    template=(
                        "System: You are a helpful AI assistant.\n"
                        "Use the short-term memory to assist the user.\n\n"
                        "Short-term memory:\n{short_term_history}\n\n"
                        "User: {user_input}\n"
                    ),
                )

                chain = prompt | llm
                response = chain.invoke({"user_input": user_input, "short_term_history": short_term_history_text})
                asyncio.run(memory_decider.save_to_memory(llm=llm, session_id=session_id, user_input=user_input,
                                              output=response.content, user_conversation=user_input))
                print("ChatBot:>", response.content)
        except Exception as e:
            print(f"Error in CLI chat: {e}")
