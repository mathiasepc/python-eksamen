import streamlit as st

st.set_page_config(
    page_title="PokeExplorer",
    page_icon="🔎",
    layout="wide",
)

st.title("PokeExplorer")

st.write(
    """
    Welcome to PokeExplorer.

    Use the menu on the left:
    - search for a Pokemon
    - compare multible Pokemon
    - see simpel statistic
    """
)

st.info("Backend must run on http://127.0.0.1:8001")