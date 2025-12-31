import gradio as gr
from src.chatbot.chatbot import ChatBot

def chat(message, history):
    chatbot = ChatBot()
    return chatbot.chat(message,"WEB")

gr.ChatInterface(chat, title="Kara").launch()