import numpy as np
import pandas as pd

from app.models.pokemon import PokemonResponse
from app.models.stats import MaxStatPokemon, StatsResponse


def pokemon_to_row(pokemon: PokemonResponse) -> dict:
    stats = pokemon.stats

    # return a row of pokemon data.
    return {
        "name": pokemon.name,
        "hp": stats.hp,
        "attack": stats.attack,
        "defense": stats.defense,
        "speed": stats.speed,
        "special_attack": stats.special_attack,
        "special_defense": stats.special_defense,
    }


def create_stats_dataframe(pokemon_list: list[PokemonResponse]) -> pd.DataFrame:
    rows = [pokemon_to_row(pokemon) for pokemon in pokemon_list]

    # Add pokemon rows to DataFrame.
    return pd.DataFrame(rows)


def create_stats_summary(pokemon_list: list[PokemonResponse]) -> StatsResponse:
    df = create_stats_dataframe(pokemon_list)

    # If no pokemon found
    if df.empty:
        empty_stat = MaxStatPokemon(name="N/A", value=0)

        return StatsResponse(
            pokemon_count=0,
            max_attack=empty_stat,
            max_speed=empty_stat,
            max_hp=empty_stat,
            max_defense=empty_stat,
            max_special_attack=empty_stat,
            max_special_defense=empty_stat,
        )

    # Get the fastest pokemon
    max_speed = int(np.amax(df["speed"]))
    max_attack = int(np.amax(df["attack"]))
    max_hp = int(np.amax(df["hp"]))
    max_defense = int(np.amax(df["defense"]))
    max_special_attack = int(np.amax(df["special_attack"]))
    max_special_defense = int(np.amax(df["special_defense"]))

    # find the row with max value.
    fastest_pokemon = df[df["speed"] == max_speed].iloc[0]
    strongest_attack_pokemon = df[df["attack"] == max_attack].iloc[0]
    most_hp_pokemon = df[df["hp"] == max_hp].iloc[0]
    strongest_defense_pokemon = df[df["defense"] == max_defense].iloc[0]
    strongest_special_attack = df[df["special_attack"] == max_special_attack].iloc[0]
    strongest_special_defense = df[df["special_defense"] == max_special_defense].iloc[0]

    # Returns a average stats object.
    return StatsResponse(
        pokemon_count=int(len(df)),
        max_attack=MaxStatPokemon(
            name=str(strongest_attack_pokemon["name"]).title(),
            value=max_attack,
        ),
        max_speed=MaxStatPokemon(
            name=str(fastest_pokemon["name"]).title(),
            value=max_speed,
        ),
        max_hp=MaxStatPokemon(
            name=str(most_hp_pokemon["name"]).title(),
            value=max_hp,
        ),
        max_defense=MaxStatPokemon(
            name=str(strongest_defense_pokemon["name"]).title(),
            value=max_defense,
        ),
        max_special_attack=MaxStatPokemon(
            name=str(strongest_special_attack["name"]).title(),
            value=max_special_attack,
        ),
        max_special_defense=MaxStatPokemon(
            name=str(strongest_special_defense["name"]).title(),
            value=max_special_defense,
        ),
    )
