from lymt.prompt import PromptManager
from lymt.chat.openai_chat import OpenAIChatManager


class OpenAIModel:
    def __init__(self, api_key: str, **kwargs):
        if not api_key:
            raise ValueError("API key is required (api_key)")

        self.api_key = api_key
        self.prompt = PromptManager()
        self.chat = OpenAIChatManager(api_key=self.api_key, prompt=self.prompt, **kwargs)
