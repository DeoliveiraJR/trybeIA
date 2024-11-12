import google.generativeai as genai
import os
import gradio as gd

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()
chat.send_message("Vocé é charles chaplin e estamos nos comunicando via mensagem, somos amigos de anos e toda vez voce inicia a conversa me contando sobre a vida no passado")


def gd_wrapper(message, _history):
    response = chat.send_message(message)
    return response.text


chatInterface = gd.ChatInterface(gd_wrapper)
chatInterface.launch()