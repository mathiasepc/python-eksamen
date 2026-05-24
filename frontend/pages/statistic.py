import os

import requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8001")

st.set_page_config(
    page_title="Statistic",
    page_icon="📊",
    layout="wide",
)

st.title("Statistic")

names_input = st.text_input(
    "Input: Pokemon-names seperated by comma",
    value="pikachu,charizard,bulbasaur",
)

if st.button("Calculate statistic"):
    response = requests.get(
        f"{BACKEND_URL}/api/stats/summary",
        params={"names": names_input},
        timeout=20,
    )

    if response.status_code == 200:
        summary = response.json()

        st.metric("Number of Pokemon", str(summary["pokemon_count"]))

        col1, col2, col3, col4 = st.columns(4)

        # Displayed vertically
        with col1:
            st.metric("Most attack", summary["max_attack"]["value"], summary["max_attack"]["name"])

        with col2:
            st.metric("Fastest", summary["max_speed"]["value"], summary["max_speed"]["name"])

        with col3:
            st.metric("Most HP", summary["max_hp"]["value"], summary["max_hp"]["name"])

        with col4:
            st.metric(
                "Most defense", summary["max_defense"]["value"], summary["max_defense"]["name"]
            )

        col5, col6 = st.columns(2)

        with col5:
            st.metric(
                "Most special attack",
                summary["max_special_attack"]["value"],
                summary["max_special_attack"]["name"],
            )

        with col6:
            st.metric(
                "Most special defense",
                summary["max_special_defense"]["value"],
                summary["max_special_defense"]["name"],
            )
    else:
        try:
            detail = response.json().get("detail", "Unkown error")
        except ValueError:
            detail = response.text

        st.error(f"Error from backend: {detail}")
