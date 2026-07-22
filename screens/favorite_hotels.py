import streamlit as st
from database.database import (
    get_favorites,
    delete_favorite
)


def show():

    st.title("❤️ Favorite Hotels")

    hotels = get_favorites()

    if len(hotels) == 0:

        st.info("No Favorite Hotels Yet.")

        return

    for hotel in hotels:

        hotel_id = hotel[0]

        st.subheader(hotel[1])

        st.write(f"📍 {hotel[2]}")

        st.write(f"⭐ {hotel[3]}")

        st.write(f"💰 ₹{hotel[4]}")

        st.write(f"🏨 {hotel[5]}")

        if st.button(
            "🗑 Remove",
            key=hotel_id
        ):

            delete_favorite(hotel_id)

            st.success("Removed Successfully")

            st.rerun()

        st.divider()
        