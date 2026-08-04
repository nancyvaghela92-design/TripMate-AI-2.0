import streamlit as st
from database.database import (
    total_trips,
    total_favorites,
    most_popular_destination,
    average_travelers
)


def show():

    st.markdown("""
    <div class="hero">

    <h1>🌍 TripMate AI 2.0</h1>

    <p>
    Plan smarter. Travel better.<br>
    Create AI-powered itineraries, discover hotels,<br>
    track budgets, and explore the world with confidence.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✈ Start Planning", use_container_width=True):
            st.session_state.page = "🗺 Trip Planner"
            st.rerun()

    with col2:
        if st.button("🌎 Explore Destinations", use_container_width=True):
            st.session_state.page = "🏨 Hotels"
            st.rerun()
    st.write("")

    st.subheader("📊 Dashboard Overview")
    st.caption("Track your trips and travel activity at a glance.")

    d1, d2 = st.columns(2)

    with d1:
        st.metric("🗺 Trips", total_trips())

    with d2:
        st.metric("❤️ Favorites", total_favorites())

    d3, d4 = st.columns(2)

    with d3:
        st.metric("🌍 Top Destination", most_popular_destination())

    with d4:
        st.metric("👨‍👩‍👧 Avg Travelers", average_travelers())

    st.divider()

    st.header("📊 TripMate Statistics")

    c1, c2 = st.columns(2)

    c1.metric("🌍 Destinations", "500+")
    c2.metric("🏨 Hotels", "2000+")

    c3, c4 = st.columns(2)

    c3.metric("👥 Users", "10K+")
    c4.metric("⭐ Rating", "4.1")

    st.divider()

    st.header("🔥 Popular Destinations")

    col1,col2=st.columns(2)

    with col1:

        st.image("assets/images/manali.jpg",use_container_width=True)

        st.subheader("🏔 Manali")

        st.write("Best Time : March - June")

    with col2:

        st.image("assets/images/goa.jpg",use_container_width=True)

        st.subheader("🏖 Goa")

        st.write("Best Time : November - February")

    st.write("")

    col3,col4=st.columns(2)

    with col3:

        st.image("assets/images/paris.jpg",use_container_width=True)

        st.subheader("🗼 Paris")

        st.write("Best Time : April - June")

    with col4:

        st.image("assets/images/japan.jpg",use_container_width=True)

        st.subheader("🗻 Japan")

        st.write("Best Time : October - November")

    st.divider()

    st.subheader("✨ Why Choose TripMate AI?")

    left, right = st.columns(2)

    with left:
        st.success("🤖 AI Travel Planner")
        st.success("🏨 Hotel Recommendations")
        st.success("🌤 Live Weather")

    with right:
        st.success("💰 Budget Calculator")
        st.success("❤️ Save Favorite Hotels")
        st.success("📄 PDF & Excel Export")

    st.divider()

    st.markdown(
    """
    <div style="text-align:center; color:gray; padding:20px;">
        <h4>✈️ TripMate AI 2.0</h4>
        <p>Developed by <b>Nancy Vaghela</b></p>
        <p>Powered by Python • Streamlit • Gemini AI</p>
        <p>© 2026 All Rights Reserved</p>
    </div>
    """,
    unsafe_allow_html=True
    )