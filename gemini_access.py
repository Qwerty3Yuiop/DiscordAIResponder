import google.generativeai as genai
import os

class AISession:
    model = None
    chat = None
    def __init__(self, model:str="gemini-1.5-flash"):
        # gets key from your env variables
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        self.model = genai.GenerativeModel(model_name=model)
        self.chat = self.model.start_chat()
    
    def send(self, prompt:str) -> str:
        text_response = []
        responses = self.chat.send_message(prompt, stream=True)
        for chunk in responses:
            text_response.append(chunk.text)
        return "".join(text_response)