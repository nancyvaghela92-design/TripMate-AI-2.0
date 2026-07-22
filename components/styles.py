import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:#F5F7FA;
    }

    .hero{
        background:linear-gradient(135deg,#0F172A,#2563EB);
        padding:45px;
        border-radius:20px;
        color:white;
        text-align:center;
        margin-bottom:30px;
    }

    .hero h1{
        color:white;
        font-size:55px;
    }

    .hero p{
        font-size:22px;
    }

    .card{
        background:white;
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0px 5px 15px rgba(0,0,0,.15);
    }

    </style>
    """, unsafe_allow_html=True)
    