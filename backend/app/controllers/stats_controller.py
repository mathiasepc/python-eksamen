from fastapi import APIRouter, HTTPException

from app.models.pokemon import PokemonResponse
from app.models.stats import StatsResponse
from app.services.pokeapi_service import get_pokemon
from app.services.stats_service import create_stats_summary

router = APIRouter(prefix="/api/stats", tags=["stats"])


@router.get("/summary", response_model=StatsResponse)
async def get_stats_summary(names: str) -> StatsResponse:
    pokemon_names = [name.strip() for name in names.split(",") if name.strip()]

    # Control checks
    if len(pokemon_names) < 2:
        raise HTTPException(
            status_code=400,
            detail="You must provide at least two Pokémon names.",
        )

    if len(pokemon_names) > 10:
        raise HTTPException(
            status_code=400,
            detail="You can analyze a maximum of ten Pokémon.",
        )

    pokemon_list: list[PokemonResponse] = []

    try:
        # Add to pokemon_list
        for name in pokemon_names:
            pokemon = await get_pokemon(name)
            pokemon_list.append(pokemon)

        return create_stats_summary(pokemon_list)
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
