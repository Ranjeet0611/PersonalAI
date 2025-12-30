import uuid

from langchain_core.prompts import PromptTemplate

from src.memory.short_term_memory import ShortTermMemory
from src.ollama.ollama import Ollama


class ChatBot:

    def get_session_id(self):
        return str(uuid.uuid4())

    def chat(self):
        try:
            ollama_model = Ollama()
            chatbot = ChatBot()
            session_id = chatbot.get_session_id()
            short_term_memory = ShortTermMemory()
            while True:
                user_input = input("You:> ")
                if "exit" in user_input:
                    short_term_memory.clear_short_term_memory(session_id=session_id)
                    break
                llm = ollama_model.get_model()
                short_term_history = short_term_memory.get_short_term_memory(session_id)

                if short_term_history:
                    short_term_history_text = "\n".join(
                        f"{m['role']}: {m['content']}" for m in short_term_history
                    )
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
                short_term_memory.save_into_memory(session_id=session_id, user_input=user_input,
                                                   output=response.content)
                print("ChatBot:>", response.content)
        except Exception as e:
            print(f"Error during chat: {e}")
