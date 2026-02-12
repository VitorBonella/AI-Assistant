from app.interfaces.llm_provider import ILLMProvider
from app.core.entities import ChatMessage

class AIAssistant:
    def __init__(self, provider: ILLMProvider):
        self.provider = provider 

    def execute(self, user_input: str) -> ChatMessage:
        response_text = self.provider.ask(user_input)
        return ChatMessage(role="assistant", content=response_text)