import streamlit as st

from database.database import (
    get_all_trips,
    delete_trip
)

from utils.excel_generator import create_excel


def show():

    st.title("❤️ Saved Trips")

    trips = get_all_trips()

    if len(trips) == 0:
        st.info("No trips saved yet.")
        return

    # Create Excel file
    excel_file = create_excel(trips)

    with open(excel_file, "rb") as file:

        st.download_button(
            label="📊 Download Saved Trips (Excel)",
            data=file,
            file_name="TripMate_Saved_Trips.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    st.divider()

    st.write(f"Total Saved Trips : {len(trips)}")

    st.divider()

    for trip in trips:

        trip_id = trip[0]
        destination = trip[1]
        budget = trip[2]
        travelers = trip[3]
        travel_type = trip[4]
        itinerary = trip[5]
        created_at = trip[6]

        with st.expander(f"📍 {destination}"):
            st.write(f"🕒 Saved On : {created_at}")
            st.write(f"💰 Budget : {budget}")
            st.write(f"👨‍👩‍👧 Travelers : {travelers}")
            st.write(f"✈️ Travel Type : {travel_type}")

            st.divider()

            st.markdown(itinerary)

            if st.button(
                "🗑 Delete Trip",
                key=f"delete_{trip_id}"
            ):

                delete_trip(trip_id)

                st.success("Trip Deleted!")

                st.rerun()