import streamlit as st
from services.hotel_service import get_hotels
from database.database import save_favorite


def show():

    st.title("🏨 Hotel Recommendations")

    destination = st.text_input(
        "Enter Destination",
        placeholder="Goa"
    )

    # Store hotels in session_state
    if "hotels" not in st.session_state:
        st.session_state.hotels = None

    if st.button("🔍 Search Hotels"):

        st.session_state.hotels = get_hotels(destination)

    hotels = st.session_state.hotels

    if hotels is not None:

        if hotels.empty:

            st.warning("No hotels found.")

        else:

            st.success(f"{len(hotels)} Hotels Found")

            for _, hotel in hotels.iterrows():

                with st.container(border=True):

                    st.subheader(hotel["Hotel"])

                    st.write(f"⭐ Rating : {hotel['Rating']}")

                    st.write(f"💰 ₹ {hotel['Price']} / Night")

                    st.write(f"🏨 Type : {hotel['Type']}")

                    if st.button(
                        f"❤️ Add {hotel['Hotel']}",
                        key=f"fav_{hotel['Hotel']}"
                    ):

                        save_favorite(
                            hotel["Hotel"],
                            hotel["Destination"],
                            hotel["Rating"],
                            hotel["Price"],
                            hotel["Type"]
                        )

                        st.success("✅ Hotel Added to Favorites!")