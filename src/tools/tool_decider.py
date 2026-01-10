from src.tools.web_search import search_web
from src.tools.flight_status import get_flight_status
from src.tools.url_shortner import shorten_url
from ollama import chat
from src.constant import constant

class ToolDecider:
    def __init__(self):
        self.tools = [search_web,get_flight_status,shorten_url]
        self.is_tool_called = False

    def decide(self, user_input,short_term_history=""):
        try:
            messages = [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "system", "content": f"Short-term memory:\n{short_term_history}"},
                {"role": "user", "content": user_input},
            ]
            response = chat(model=constant.OLLAMA_MODEL_NAME, messages=messages, tools=self.tools)
            if response.message.tool_calls:
                self.is_tool_called = True
                for call in response.message.tool_calls:
                    if call.function.name == "search_web":
                        result = search_web(**call.function.arguments)
                        print(f"Web Search Result: {result}")
                    elif call.function.name == "get_flight_status":
                        result = get_flight_status(**call.function.arguments)
                        print(f"Flight Status Result: {result}")
                    elif call.function.name == "shorten_url":
                        result = shorten_url(**call.function.arguments)
                        print(f"URL Shortener Result: {result}")
                    else:
                        result = "Tool not recognized."
                    messages.append({'role': 'tool', 'tool_name': call.function.name, 'content': str(result)})
                final_response = chat(model=constant.OLLAMA_MODEL_NAME, messages=messages, tools=self.tools)
                return {'response':final_response.message,'tool_used':self.is_tool_called}
            return {'response':'','tool_used':self.is_tool_called}
        except Exception as e:
            print(f"Error initializing tools: {e}")
            return None
