from google import genai
from google.genai import types
from app.interfaces.llm_provider import ILLMProvider
from app.infrastructure.tools.calculator import calculate

class GeminiProvider(ILLMProvider):
    def __init__(self, api_key: str, model_name: str):
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name
       

    def ask(self, prompt: str) -> str:
        response = self.client.models.generate_content(
                        model= self.model_name ,
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            tools=[calculate]
                        ),
                    )
        

        return response.text