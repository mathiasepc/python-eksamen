import os

from dotenv import load_dotenv
from openai import OpenAI

from app.models.pokemon import PokemonResponse

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def build_pokemon_context(pokemon: PokemonResponse) -> str:
    return f"""
Pokemon data:
Name: {pokemon.name}
Types: {", ".join(pokemon.types)}
Abilities: {", ".join(pokemon.abilities)}
Height: {pokemon.height}
Weight: {pokemon.weight}
Stats:
- HP: {pokemon.stats.hp}
- Attack: {pokemon.stats.attack}
- Defense: {pokemon.stats.defense}
- Special attack: {pokemon.stats.special_attack}
- Special defense: {pokemon.stats.special_defense}
- Speed: {pokemon.stats.speed}
""".strip()


def ask_openai_about_pokemon(pokemon: PokemonResponse, question: str) -> str:
    context = build_pokemon_context(pokemon)

    response = client.responses.create(
        model="gpt-4.1-mini",
        max_output_tokens=300,
        input=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant for a school project called PokéExplorer. "
                    "Answer questions using the provided Pokémon data as context. "
                    "If the question cannot be answered from the data, say so clearly."
                    "Keep answers under 8 sentences."
                ),
            },
            {
                "role": "user",
                "content": f"{context}\n\nUser question: {question}",
            },
        ],
    )

    return response.output_text
