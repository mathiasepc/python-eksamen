import os

import httpx
from dotenv import load_dotenv

from app.models.pokemon import PokemonResponse, PokemonStats

load_dotenv()

POKEAPI_BASE_URL = os.getenv("POKEAPI_BASE_URL", "https://pokeapi.co/api/v2")


def parse_pokemon_response(data: dict) -> PokemonResponse:
    stats_dict = {stat_item["stat"]["name"]: stat_item["base_stat"] for stat_item in data["stats"]}

    # Stats for indivdual pokemons
    stats = PokemonStats(
        hp=stats_dict["hp"],
        attack=stats_dict["attack"],
        defense=stats_dict["defense"],
        special_attack=stats_dict["special-attack"],
        special_defense=stats_dict["special-defense"],
        speed=stats_dict["speed"],
    )

    # The specific pokemon
    return PokemonResponse(
        name=data["name"],
        types=[type_item["type"]["name"] for type_item in data["types"]],
        abilities=[ability_item["ability"]["name"] for ability_item in data["abilities"]],
        height=data["height"],
        weight=data["weight"],
        stats=stats,
        # Count all stats from PokemonStats
        total_stats=sum(stats.model_dump().values()),
    )


async def get_pokemon(name: str) -> PokemonResponse:
    pokemon_name = name.strip().lower()

    if not pokemon_name:
        raise Exception("Pokémon name cannot be empty.")

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f"{POKEAPI_BASE_URL}/pokemon/{pokemon_name}")

    if response.status_code == 404:
        raise Exception(f"Pokémon '{name}' was not found.")

    return parse_pokemon_response(response.json())
