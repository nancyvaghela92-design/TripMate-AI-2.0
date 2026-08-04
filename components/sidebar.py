import streamlit as st

PAGES = [
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

def show_sidebar():

    st.sidebar.title("✈️ TripMate AI 2.0")

    # Default page
    if "page" not in st.session_state:
        st.session_state.page = "🏠 Home"

    page = st.sidebar.radio(
        "Navigation",
        PAGES,
        index=PAGES.index(st.session_state.page)
    )

    st.session_state.page = page

    st.sidebar.divider()

    theme = st.sidebar.toggle(
        "🌙 Dark Mode",
        value=st.session_state.get("dark_mode", False)
    )

    st.session_state.dark_mode = theme

    return page