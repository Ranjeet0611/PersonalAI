from src.tools.web_search import search_web
from ollama import chat
from src.constant import constant

class ToolDecider:
    def __init__(self):
        self.tools = [search_web]
        self.is_tool_called = False

    def decide(self, user_input):
        try:
            messages = [{"role": "user", "content": user_input}]
            response = chat(model=constant.OLLAMA_MODEL_NAME, messages=messages, tools=self.tools)

            if response.message.tool_calls:
                self.is_tool_called = True
                for call in response.message.tool_calls:
                    if call.function.name == "search_web":
                        result = search_web(**call.function.arguments)
                        print(f"Web Search Result: {result}")
                    else:
                        result = "Tool not recognized."
                    messages.append({'role': 'tool', 'tool_name': call.function.name, 'content': str(result)})
                final_response = chat(model=constant.OLLAMA_MODEL_NAME, messages=messages, tools=self.tools)
                return {'response':final_response.message,'tool_used':self.is_tool_called}
            return {'response':'','tool_used':self.is_tool_called}
        except Exception as e:
            print(f"Error initializing tools: {e}")
            return None
