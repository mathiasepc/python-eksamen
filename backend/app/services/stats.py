import numpy as np
import pandas as pd

from app.models.pokemon import PokemonResponse

def pokemon_to_row(pokemon: PokemonResponse) -> dict:
    stats = pokemon.stats;
    
    return {
        "name": pokemon.name,
        "hp": stats.hp,
        "attack": stats.attack,
        "defense": stats.defense,
        "special_attack": stats.special_attack,
        "special_defense": stats.special_defense,
        "speed": stats.speed
    };
    
def create_stats_dataframe(pokemon_list: list[PokemonResponse]) -> pd.DataFrame:
    rows = {
        pokemon_to_row(pokemon)
        for pokemon in pokemon_list
    };
    
    return pd.DataFrame(rows);

def create_stats_summary(pokemon_list: list[PokemonResponse]) -> dict:
    df = create_stats_dataframe(pokemon_list);
    
    if df.empty:
        return {
            "pokemon_count": 0,
            "average_attack": 0,
            "average_defense": 0,
            "average_speed": 0,
            "strongest_pokemon": None,
            "fastest_pokemon": None
        };
    
    strongest_index = df["total_stats"].idxmax();
    fastest_index = df["speed"].idxmax();
    
    return {
        "pokemon_count": int(len(df)),
        "average_attack": float(np.mean(df["attack"])),
        "average_defense": float(np.mean(df["defense"])),
        "average_speed": float(np.mean(df["speed"])),
        "strongest_pokemon": str(df.loc[strongest_index, "name"]),
        "fastest_pokemon": str(df.loc[fastest_index, "name"]),
        "total_stats_by_pokemon": df.set_index("name")["total_stats"].to_dict(),
    }
    
    