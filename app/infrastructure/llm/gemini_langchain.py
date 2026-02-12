from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from app.interfaces.llm_provider import ILLMProvider
import os
from app.infrastructure.tools.calculator import calculate

class GeminiLangchainProvider(ILLMProvider):
    def __init__(self, api_key: str, model_name: str):
        os.environ["GOOGLE_API_KEY"] = api_key
        self.model = ChatGoogleGenerativeAI(model=model_name).bind_tools([calculate])
       

    def ask(self, prompt: str) -> str:
        messages = [HumanMessage(prompt)]
        ai_msg = self.model.invoke(messages)
        if not ai_msg.tool_calls:
            return ai_msg.content
        messages.append(ai_msg)
                
        print(ai_msg.tool_calls)

        for tool_call in ai_msg.tool_calls:
            tool_result = calculate.invoke(tool_call)
            messages.append(tool_result)

        final_response = self.model.invoke(messages)
        print(final_response)
        return final_response.text