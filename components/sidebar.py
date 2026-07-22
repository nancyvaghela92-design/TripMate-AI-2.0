import streamlit as st

def show_sidebar():

    st.sidebar.title("✈️ TripMate AI 2.0")

    page = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Home",
            "🤖 AI Assistant",
            "🗺 Trip Planner",
            "🏨 Hotels",
            "💰 Budget",
            "🌤 Weather",
            "❤️ Saved Trips",
            "❤️ Favorite Hotels",
            "ℹ About"
        ]
    )

    st.sidebar.divider()

    theme = st.sidebar.toggle("🌙 Dark Mode")

    st.session_state.dark_mode = theme

    return page