from lymt.prompt import PromptManager
from lymt.chat.ollama_chat import OllamaChatManager


class OllamaModel:
    def __init__(self, **kwargs):
        self.prompt = PromptManager()
        self.chat = OllamaChatManager(self.prompt, **kwargs)
