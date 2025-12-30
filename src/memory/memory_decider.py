from langchain_classic.prompts import ChatPromptTemplate
from src.memory.short_term_memory import ShortTermMemory


class MemoryDecider(object):
    def save_to_memory(self, llm, session_id, user_input, output, user_conversation):
        try:
            prompt_template = ChatPromptTemplate([("system",
                                                   "You're a helpful AI assistant. Decide whether to store the following user conversation in short-term or long-term memory or no need to store. If the information is already stored, do not store it again. Respond with only 'short-term', 'long-term', or 'None'."),
                                                  ("human", f"{user_conversation}")])
            chain = prompt_template | llm
            response = chain.invoke({"user_input": user_conversation})
            if "short-term" in response.content.lower():
                short_term_memory = ShortTermMemory()
                short_term_memory.save_into_memory(session_id=session_id, user_input=user_input, output=output)
        except Exception as e:
            print(f"Failed to decide memory: {e}")
