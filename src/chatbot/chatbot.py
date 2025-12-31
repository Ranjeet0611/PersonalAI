from src.chatbot.cli_chatbot import CLIChatbot
from src.chatbot.web_chatbot import WebChatbot
from src.constant import constant


class ChatBot:
    def chat(self, user_input=None, app_type="CLI"):
        client_chatbot = CLIChatbot()
        web_chatbot = WebChatbot()
        try:
            if app_type == constant.CLI_APP_TYPE:
                client_chatbot.cli_chat()
                return None
            elif app_type == constant.WEB_APP_TYPE:
                return web_chatbot.web_chat(user_input=user_input)
            else:
                return None
        except Exception as e:
            print(f"Error during chat: {e}")
            return "Error during chat."
