from services.ai_service import generate_trip
import streamlit as st
from datetime import date
from database.database import save_trip
from utils.pdf_generator import create_pdf


def show():

    st.title("🗺️ Smart Trip Planner")
    st.write("Fill in your travel details below.")
    st.divider()

    destination = st.text_input(
        "📍 Destination",
        placeholder="Example: Goa"
    )

    start_date = st.date_input(
        "📅 Start Date",
        value=date.today()
    )

    end_date = st.date_input(
        "📅 End Date",
        value=date.today()
    )

    budget = st.selectbox(
        "💰 Budget",
        ["Low", "Medium", "Luxury"]
    )

    travelers = st.number_input(
        "👨‍👩‍👧 Number of Travelers",
        min_value=1,
        max_value=20,
        value=2
    )

    travel_type = st.selectbox(
        "✈️ Travel Type",
        ["Solo", "Family", "Friends", "Couple"]
    )

    # ---------------- Generate Trip ----------------

    if st.button("🚀 Generate Trip", use_container_width=True):

        st.success("Trip Plan Generated Successfully!")

        st.subheader("📋 Trip Summary")

        st.write(f"📍 Destination : {destination}")
        st.write(f"📅 Start Date : {start_date}")
        st.write(f"📅 End Date : {end_date}")
        st.write(f"💰 Budget : {budget}")
        st.write(f"👨‍👩‍👧 Travelers : {travelers}")
        st.write(f"✈️ Travel Type : {travel_type}")

        st.divider()

        with st.spinner("🤖 Generating AI Trip..."):

            trip = generate_trip(
                destination,
                budget,
                travelers,
                travel_type
            )

        st.session_state.trip = trip

    # ---------------- Show Trip ----------------

    if "trip" in st.session_state:

        st.subheader("🤖 AI Travel Plan")

        st.markdown(st.session_state.trip)

        pdf_file = create_pdf(st.session_state.trip)

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📄 Download Trip as PDF",
                data=file,
                file_name="TripMate_Itinerary.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    # ---------------- Save Trip ----------------

    if st.button("💾 Save Trip", use_container_width=True):

        if "trip" not in st.session_state:

            st.warning("⚠️ Please generate a trip first.")

        else:

            save_trip(
                destination,
                budget,
                travelers,
                travel_type,
                st.session_state.trip
            )

            st.success("✅ Trip Saved Successfully!")