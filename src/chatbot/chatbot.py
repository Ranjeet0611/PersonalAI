import uuid

from langchain_core.prompts import PromptTemplate

from src.memory.memory_decider import MemoryDecider
from src.memory.short_term_memory import ShortTermMemory
from src.ollama.ollama import Ollama


class ChatBot:

    def get_session_id(self):
        return str(uuid.uuid4())

    def get_conversation(self, user_input, output):
        messages = [{"role": "user", "content": user_input}, {"role": "assistant", "content": output}]
        conversation = "\n".join(
            f"{m['role']}: {m['content']}" for m in messages
        )
        return conversation

    def chat(self):
        try:
            ollama_model = Ollama()
            session_id = self.get_session_id()
            short_term_memory = ShortTermMemory()
            memory_decider = MemoryDecider()
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
                conversation = self.get_conversation(user_input, response.content)
                memory_decider.save_to_memory(llm=llm, session_id=session_id, user_input=user_input,
                                              output=response.content, user_conversation=conversation)
                print("ChatBot:>", response.content)
        except Exception as e:
            print(f"Error during chat: {e}")
