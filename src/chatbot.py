import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # Load environment variables from .env

class Chatbot:
    def __init__(self, memory, model="gemini-1.5-flash"):
        self.memory = memory
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")
        self.llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key)

    def generate_response(self, user_input):
        history = self.memory.retrieve_memory()
        prompt = f"{history}\nHuman: {user_input}\nAI:"
        response = self.llm.invoke(prompt)
        # Handle dict response with "content" key
        if isinstance(response, dict) and "content" in response:
            response_text = response["content"]
            # Remove leading "content=" if present
            if response_text.startswith("content="):
                response_text = response_text[len("content="):].strip("'\" ")
        elif hasattr(response, "content"):
            response_text = str(response.content)
            if response_text.startswith("content="):
                response_text = response_text[len("content="):].strip("'\" ")
        elif isinstance(response, dict) and "text" in response:
            response_text = str(response["text"])
        else:
            response_text = str(response)
        self.memory.add_memory(user_input, response_text)
        return response_text

    def set_memory(self, memory):
        self.memory = memory

    def get_memory(self):
        return self.memory.retrieve_memory()