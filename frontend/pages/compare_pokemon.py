import pandas as pd
import requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8001"

# Title of page config
st.set_page_config(
    page_title="Compare Pokemon",
    page_icon="⚔️",
    layout="wide",
)

# page title
st.title("Compare Pokemon")

# input filed
names_input = st.text_input(
    "Input: 2-4 Pokemon-names seperated by comma",
    # place holder
    value="pikachu,charizard",
)

# button logic
if st.button("Compare"):
    response = requests.get(
        f"{BACKEND_URL}/api/pokemon/compare",
        params={"names": names_input},
        timeout=20,
    )

    # success
    if response.status_code == 200:
        pokemon_list = response.json()

        rows = []

        # set rows
        for pokemon in pokemon_list:
            stats = pokemon["stats"]

            rows.append(
                {
                    "name": pokemon["name"],
                    "hp": stats["hp"],
                    "attack": stats["attack"],
                    "defense": stats["defense"],
                    "special_attack": stats["special_attack"],
                    "special_defense": stats["special_defense"],
                    "speed": stats["speed"],
                    "total_stats": pokemon["total_stats"],
                }
            )

        # set DataFrame
        df = pd.DataFrame(rows)

        # Data section
        st.write("### Data")
        st.dataframe(df, use_container_width=True)

        # Base stats
        st.write("### Base stats")
        # set chart
        chart_df = df.set_index("name")[
            [
                "hp",
                "attack",
                "defense",
                "special_attack",
                "special_defense",
                "speed",
            ]
        ]

        # Display chart
        st.bar_chart(chart_df)

        # Total stats comined
        st.write("### Total stats")
        st.bar_chart(df.set_index("name")["total_stats"])

    else:
        try:
            detail = response.json().get("detail", "Unkown error")
        except ValueError:
            detail = response.text

        st.error(f"Error from backend: {detail}")