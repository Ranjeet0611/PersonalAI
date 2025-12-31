from langchain_classic.prompts import ChatPromptTemplate
from src.memory.short_term_memory import ShortTermMemory
from src.memory.long_term_memory import LongTermMemory


class MemoryDecider(object):
    def save_to_memory(self, llm, session_id, user_input, output, user_conversation):
        try:
            system_prompt = ""
            with open("storage_prompt.txt","r") as file:
                system_prompt = file.read()
            prompt_template = ChatPromptTemplate([("system", f"{system_prompt}"),
                                                  ("human", f"{user_conversation}")])
            chain = prompt_template | llm
            response = chain.invoke({"user_input": user_conversation})
            print("Memory decider ",response.content)
            if "short-term" in response.content.lower():
                short_term_memory = ShortTermMemory()
                short_term_memory.save_into_memory(session_id=session_id, user_input=user_input, output=output)
            elif "long-term" in response.content.lower():
                long_term_memory = LongTermMemory()
                long_term_memory.save_into_memory(user_input=user_input, output=output)
        except Exception as e:
            print(f"Failed to decide memory: {e}")
