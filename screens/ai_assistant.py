import streamlit as st
from services.chat_service import chat_with_ai


def show():

    st.title("🤖 TripMate AI Assistant")

    st.write("Ask anything about travel.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask TripMate AI...")

    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("TripMate AI is thinking..."):

            reply = chat_with_ai(
                user_input,
                st.session_state.messages
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        with st.chat_message("assistant"):
            st.markdown(reply)

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()