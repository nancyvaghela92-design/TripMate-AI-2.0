import streamlit as st

def load_css():

    dark = st.session_state.get("dark_mode", False)

    if dark:
        bg = "#0F172A"
        card = "#1E293B"
        text = "#FFFFFF"
        hero = "linear-gradient(135deg,#111827,#2563EB)"
        shadow = "0 8px 25px rgba(0,0,0,.35)"
    else:
        bg = "#F5F7FA"
        card = "#FFFFFF"
        text = "#111827"
        hero = "linear-gradient(135deg,#0F172A,#2563EB)"
        shadow = "0 8px 25px rgba(0,0,0,.15)"

    st.markdown(f"""
    <style>

    .stApp {{
        background: {bg};
        color: {text};
        transition: all .3s ease;
    }}

    .hero {{
        background: {hero};
        padding:50px;
        border-radius:25px;
        color:white;
        text-align:center;
        margin-bottom:30px;
        box-shadow:{shadow};
    }}

    .hero h1 {{
        color:white;
        font-size:58px;
        margin-bottom:10px;
    }}

    .hero p {{
        color:white;
        font-size:22px;
    }}

    div[data-testid="stMetric"] {{
        background:{card};
        border-radius:18px;
        padding:18px;
        box-shadow:{shadow};
        transition:0.3s;
    }}

    div[data-testid="stMetric"]:hover {{
        transform:translateY(-5px);
    }}

    .stButton > button {{
        width:100%;
        border-radius:12px;
        height:52px;
        font-size:17px;
        font-weight:600;
        transition:.3s;
    }}

    .stButton > button:hover {{
        transform:scale(1.03);
    }}

    /* Mobile */

    @media (max-width:768px) {{

        .hero {{
            padding:25px;
        }}

        .hero h1 {{
            font-size:34px;
        }}

        .hero p {{
            font-size:16px;
        }}
    }}

    </style>
    """, unsafe_allow_html=True)
    