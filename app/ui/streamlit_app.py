import streamlit as st
from app.infrastructure.llm.factory import LLMFactory
from app.core.assistant import AIAssistant
from app.core.entities import ChatMessage

st.set_page_config(page_title="AI Engineer Challenge", page_icon="🤖")

st.title("Tcafetra Bot")

with st.sidebar:
    st.header("Config")
    provider_name = st.selectbox("Choose Model", ["Gemini", "Gemini(langchain)"])
    api_key = st.text_input("API Key", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg.role):
        st.markdown(msg.content)

if prompt := st.chat_input("Ask me..."):
    if not api_key:
        st.warning("Please enter the API Key in the sidebar.")
        st.stop()


    st.session_state.messages.append(ChatMessage(role="user", content=prompt))
    with st.chat_message("user"):
        st.text_input(prompt)

    try:
        provider = LLMFactory.get_provider(provider_name, api_key)
        assistant = AIAssistant(provider)
        response = assistant.execute(prompt)
        
        st.session_state.messages.append(response)
        with st.chat_message("assistant"):
            st.text(response.content)
    except Exception as e:
        st.error(f"Error: {e}")