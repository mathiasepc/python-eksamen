from pydantic import BaseModel


# specific stats for individual pokemons
class PokemonStats(BaseModel):
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


class PokemonResponse(BaseModel):
    # Name of pokemon
    name: str
    # electric, water, flying eg.
    types: list[str]
    # Moves like solar-power, lightning ball
    abilities: list[str]
    height: int
    weight: int
    stats: PokemonStats
    # all stats accumulated
    total_stats: int
