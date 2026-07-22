import streamlit as st

def show():

    st.title("💰 Smart Budget Calculator")
    st.write("Estimate your total trip cost.")

    st.divider()

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        value=3
    )

    travelers = st.number_input(
        "👨‍👩‍👧 Number of Travelers",
        min_value=1,
        value=2
    )

    hotel = st.number_input(
        "🏨 Hotel Cost (Per Night ₹)",
        min_value=0,
        value=3000
    )

    food = st.number_input(
        "🍕 Food Cost (Per Person / Day ₹)",
        min_value=0,
        value=800
    )

    transport = st.number_input(
        "🚖 Transport Cost (₹)",
        min_value=0,
        value=2000
    )

    activities = st.number_input(
        "🎟 Activities Cost (₹)",
        min_value=0,
        value=1500
    )

    st.divider()

    if st.button("💰 Calculate Budget", use_container_width=True):

        hotel_total = hotel * days
        food_total = food * travelers * days

        total = (
            hotel_total +
            food_total +
            transport +
            activities
        )

        st.success("✅ Budget Calculated Successfully!")

        st.subheader("📊 Budget Breakdown")

        st.write(f"🏨 Hotel Cost : ₹ {hotel_total:,}")
        st.write(f"🍕 Food Cost : ₹ {food_total:,}")
        st.write(f"🚖 Transport : ₹ {transport:,}")
        st.write(f"🎟 Activities : ₹ {activities:,}")

        st.divider()

        st.metric("💰 Total Estimated Budget", f"₹ {total:,}")

        if total <= 10000:
            st.success("🟢 Budget Friendly Trip")

        elif total <= 30000:
            st.warning("🟡 Moderate Budget Trip")

        else:
            st.error("🔴 Luxury Budget Trip")