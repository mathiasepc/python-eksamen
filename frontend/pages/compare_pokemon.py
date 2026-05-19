import matplotlib.pyplot as plt
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

def create_stats_dataframe(pokemon_list: list[dict]) -> pd.DataFrame:
    rows = [];

    for pokemon in pokemon_list:
        stats = pokemon["stats"];

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
        );

    return pd.DataFrame(rows);

def plot_base_stats(df: pd.DataFrame) -> plt.Figure:
    stats_columns = [
        "hp",
        "attack",
        "defense",
        "special_attack",
        "special_defense",
        "speed",
    ];
    
    chart_df = df.set_index("name")[stats_columns];
    
    fig, ax = plt.subplots(figsize=(10,5));
    chart_df.plot(kind="bar", ax=ax);
    
    ax.set_title("Base stats sammenligning");
    ax.set_xlabel("Pokémon");
    ax.set_ylabel("Stat value");
    ax.legend(title="Stats");
    ax.tick_params(axis="x", rotation=0);

    fig.tight_layout();

    return fig;

def plot_total_stats(df: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(8,4));
    
    ax.bar(df["name"], df["total_stats"]);
    
    ax.set_title("Total stats")
    ax.set_xlabel("Pokémon")
    ax.set_ylabel("Total stats")

    fig.tight_layout()

    return fig

# button logic
if st.button("Compare"):
    response = requests.get(
        f"{BACKEND_URL}/api/pokemon/compare",
        params={"names": names_input},
        timeout=20,
    );

    # success
    if response.status_code == 200:
        pokemon_list = response.json();

        df = create_stats_dataframe(pokemon_list);

        # Data section
        st.write("### Data");
        st.dataframe(df, use_container_width=True);

        # Base stats
        st.write("### Base stats");
        base_stats_fig = plot_base_stats(df);
        st.pyplot(base_stats_fig);

        # Total stats comined
        st.write("### Total stats");
        total_stats_fig = plot_total_stats(df);
        st.pyplot(total_stats_fig);

    else:
        try:
            detail = response.json().get("detail", "Unkown error");
        except ValueError:
            detail = response.text;

        st.error(f"Error from backend: {detail}");