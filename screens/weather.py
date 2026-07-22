import streamlit as st
from services.weather_service import get_weather


def show():

    st.title("🌤 Live Weather")

    city = st.text_input(
        "Enter City",
        placeholder="Ahmedabad"
    )

    if st.button("Get Weather"):

        weather = get_weather(city)

        if weather:

            st.success("Weather Found!")

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "🌡 Temperature",
                    f"{weather['temperature']} °C"
                )

                st.metric(
                    "💧 Humidity",
                    f"{weather['humidity']} %"
                )

            with c2:

                st.metric(
                    "🌥 Condition",
                    weather["condition"]
                )

                st.metric(
                    "💨 Wind",
                    f"{weather['wind']} km/h"
                )

        else:

            st.error("City not found.")