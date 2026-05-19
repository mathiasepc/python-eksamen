import requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8001"

st.set_page_config(
    page_title="search Pokemon",
    page_icon="🔍",
    layout="wide",
);

st.title("Search Pokemon");

pokemon_name = st.text_input("Type a Pokemon-name", value="pikachu");

if st.button("Search"):
    if not pokemon_name.strip():
        st.warning("Type a Pokemon-name.");
    else:
        response = requests.get(
            f"{BACKEND_URL}/api/pokemon/{pokemon_name.strip()}",
            timeout=10,
        );

        # Success
        if response.status_code == 200:
            pokemon = response.json();

            st.subheader(pokemon["name"].title());
            
            col1, col2, col3 = st.columns(3);

            ## Display vertically
            with col1:
                st.metric("Height", pokemon["height"]);
                st.metric("Weight", pokemon["weight"]);

            with col2:
                st.write("**Types**");
                st.write(", ".join(pokemon["types"]));

            with col3:
                st.write("**Ability**");
                st.write(", ".join(pokemon["abilities"]));

            # Stats of the specific pokemon
            st.write("### Base stats");
            st.json(pokemon["stats"]);

            # all stats compined
            st.metric("Total stats", pokemon["total_stats"]);

        elif response.status_code == 404:
            st.error("Pokemon was not found.");
        else:
            st.error(f"Backend-error: {response.status_code}");