import streamlit as st
from chatbot.model import get_response

st.set_page_config(page_title="InstaHelp AI", page_icon="🤖")

st.title("🤖 InstaHelp – Fast AI Chatbot")
st.caption("Intent-based NLP • Instant replies • Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.write(msg)

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    response = get_response(user_input)

    st.session_state.messages.append(("assistant", response))
    with st.chat_message("assistant"):
        st.write(response)
