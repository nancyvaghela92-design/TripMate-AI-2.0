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

    <p>Plan Your Dream Journey With Artificial Intelligence</p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.button("✈ Start Planning", use_container_width=True)

    with col2:
        st.button("🌎 Explore Destinations", use_container_width=True)

    st.write("")

    st.header("📈 Your TripMate Dashboard")

    d1, d2, d3, d4 = st.columns(4)

    d1.metric("🗺️ Trips", total_trips())
    d2.metric("❤️ Favorites", total_favorites())
    d3.metric("🌍 Top Destination", most_popular_destination())
    d4.metric("👨‍👩‍👧 Avg Travelers", average_travelers())

    st.divider()

    st.header("📊 TripMate Statistics")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Destinations","500+")
    c2.metric("Hotels","2000+")
    c3.metric("Users","10K+")
    c4.metric("Rating","1.9⭐")

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

    st.success("🤖 AI Powered Travel Recommendations")

    st.success("💰 Budget Calculator")

    st.success("🏨 Hotel Recommendation")

    st.success("🌤 Live Weather")

    st.success("🗺 Smart Itinerary Planner")