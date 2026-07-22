import streamlit as st

from components.styles import load_css
from components.sidebar import show_sidebar
from database.database import create_table, create_favorite_table

from screens import (
    home,
    ai_assistant,
    favorite_hotels,
    planner,
    hotels,
    budget,
    weather,
    saved,
    about
)

# ---------------- Page Config ----------------

st.set_page_config(
    page_title="TripMate AI 2.0",
    page_icon="✈️",
    layout="wide"
)

# ---------------- Create Database ----------------

create_table()
create_favorite_table()

# ---------------- Sidebar ----------------

page = show_sidebar()

# ---------------- Load Theme ----------------

load_css()

# ---------------- Navigation ----------------

if page == "🏠 Home":
    home.show()

elif page == "🤖 AI Assistant":
    ai_assistant.show()

elif page == "🗺 Trip Planner":
    planner.show()

elif page == "🏨 Hotels":
    hotels.show()

elif page == "💰 Budget":
    budget.show()

elif page == "🌤 Weather":
    weather.show()

elif page == "❤️ Saved Trips":
    saved.show()

elif page == "ℹ About":
    about.show()
elif page == "❤️ Favorite Hotels":
    favorite_hotels.show()