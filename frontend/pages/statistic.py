import requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8001"

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
    );

    if response.status_code == 200:
        summary = response.json();

        col1, col2, col3 = st.columns(3);

        # Displayed vertically
        with col1:
            st.metric("Number of Pokemon", summary["pokemon_count"]);
            st.metric("Average attack", round(summary["average_attack"], 2));

        with col2:
            st.metric("Average defense", round(summary["average_defense"], 2));
            st.metric("Average speed", round(summary["average_speed"], 2));

        with col3:
            st.metric("Strongest Pokemon", summary["strongest_pokemon"]);
            st.metric("Fastest Pokemon", summary["fastest_pokemon"]);

        # Display total stats pr pokemon
        st.write("### Total stats pr. Pokemon");
        st.bar_chart(summary["total_stats_by_pokemon"]);

        # data combined from the pokemons picked
        st.write("### Raw summary");
        st.json(summary);

    else:
        try:
            detail = response.json().get("detail", "Unkown error");
        except ValueError:
            detail = response.text;

        st.error(f"Error from backend: {detail}");