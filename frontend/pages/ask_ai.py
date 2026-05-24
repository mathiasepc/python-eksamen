import os

import requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8001")

st.set_page_config(
    page_title="Ask AI",
    page_icon="🤖",
    layout="wide",
)

st.title("Ask ai about a pokemon")

st.write(
    """
    Ask a question about a pokemon
    Backend fetches Pokemon-data from PokeAPI and send the question to openAI.
    """
)

pokemon_name = st.text_input("Pokemon-name", value="charizard")

question = st.text_area(
    "Your question",
    value="Why is Charizard good offensively?",
    height=120,
)

if st.button("Ask AI"):
    if not pokemon_name:
        st.warning("You must type a pokemon name")
    elif not question:
        st.warning("You have to type a question")

    else:
        response = requests.post(
            f"{BACKEND_URL}/api/ai/ask",
            json={
                "pokemon_name": pokemon_name.strip(),
                "question": question.strip(),
            },
            timeout=60,
        )

        if response.status_code == 200:
            data = response.json()

            st.subheader(f"Answering {data['pokemon_name'].title()}")
            st.write(data["answer"])

        else:
            try:
                detail = response.json().get("detail", "Unkown error")
            except Exception:
                detail = response.text

            st.error(f"Error: {detail}")
