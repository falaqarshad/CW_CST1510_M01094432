import streamlit as st
from services.ai_assistant import AIAssistant

st.title("🤖 AI Assistant")

# Create AI assistant once per session
if "ai" not in st.session_state:
    st.session_state.ai = AIAssistant(
        system_prompt="You are an AI assistant for a university project."
    )

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for message in st.session_state.chat_history:
    role, content = message
    with st.chat_message(role):
        st.write(content)

# User input
user_input = st.chat_input("Ask the AI something...")

if user_input:
    # Show user message
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response
    response = st.session_state.ai.send_message(user_input)

    # Show AI response
    st.session_state.chat_history.append(("assistant", response))
    with st.chat_message("assistant"):
        st.write(response)