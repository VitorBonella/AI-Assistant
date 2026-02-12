from abc import ABC, abstractmethod

class ILLMProvider(ABC):
    @abstractmethod
    def ask(self, prompt: str, tools: list = None) -> str:
        """Ask models and return a response"""
        pass