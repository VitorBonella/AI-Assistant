from app.infrastructure.llm.gemini import GeminiProvider
from app.infrastructure.llm.gemini_langchain import GeminiLangchainProvider


class LLMFactory:
    @staticmethod
    def get_provider(name: str, api_key: str):
        if name.lower() == "gemini":
            return GeminiProvider(api_key=api_key,model_name="gemini-2.5-flash-lite")
        if name.lower() == "gemini(langchain)":
            return GeminiLangchainProvider(api_key=api_key,model_name="gemini-2.5-flash-lite")
        raise ValueError(f"Provedor {name} não suportado.")