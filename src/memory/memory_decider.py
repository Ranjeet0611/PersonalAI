from langchain_classic.prompts import ChatPromptTemplate
from src.memory.long_term_memory import LongTermMemory
from src.memory.short_term_memory import ShortTermMemory


class MemoryDecider(object):
    def decide_memory(self, llm, user_input: str):
        try:
            prompt_template = ChatPromptTemplate([("system",
                                                   "You're a helpful AI assistant.Decide which memory to use between short-term and long-term based on the user's input. Return only 'short-term' or 'long-term'. If you're not able to figure out just return short-term memory"),
                                                  ("human", f"{user_input}")])
            chain = prompt_template | llm
            response = chain.invoke({"user_input": user_input})
            print(response.content)
            if "long-term" in response.content.lower():
                return LongTermMemory()
            else:
                return ShortTermMemory()
        except Exception as e:
            print(f"Failed to decide memory: {e}")
            return None
