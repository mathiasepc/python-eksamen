from pydantic import BaseModel


class MaxStatPokemon(BaseModel):
    name: str
    value: int


class StatsResponse(BaseModel):
    pokemon_count: int
    max_attack: MaxStatPokemon
    max_speed: MaxStatPokemon
    max_hp: MaxStatPokemon
    max_defense: MaxStatPokemon
    max_special_attack: MaxStatPokemon
    max_special_defense: MaxStatPokemon
