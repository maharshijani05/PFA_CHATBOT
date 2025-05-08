import streamlit as st
from personal_finance_chatbot import get_chatbot_response

st.set_page_config(page_title="PFA Chatbot", page_icon="💬", layout="centered")
st.title("🤖 Personal Finance Assistant Chatbot")
st.write("Hello! Ask about your finances.")

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Get user ID from input
user_id = "6819921664cc431469081bd6"

# Chat input
user_query = st.chat_input("Ask something...")

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
if user_query and user_id:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_chatbot_response(user_id, user_query)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
