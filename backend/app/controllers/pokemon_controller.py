from fastapi import APIRouter, HTTPException

from app.models.pokemon import PokemonResponse
from app.services.pokeapi_service import get_pokemon

router = APIRouter(prefix="/api/pokemon", tags=["pokemon"])


@router.get("/compare", response_model=list[PokemonResponse])
async def compare_pokemon(names: str) -> list[PokemonResponse]:
    pokemon_names = []

    for name in names.split(","):
        cleaned_name = name.strip()

        if cleaned_name:
            pokemon_names.append(cleaned_name)

    # Control checks
    if len(pokemon_names) < 2:
        raise HTTPException(status_code=400, detail="You must provied atleast two pokemon names")

    if len(pokemon_names) > 4:
        raise HTTPException(status_code=400, detail="You can compare max of 4 pokemon")

    try:
        return [await get_pokemon(name) for name in pokemon_names]
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error)) from error


@router.get("/{name}", response_model=PokemonResponse)
async def read_pokemon(name: str) -> PokemonResponse:
    try:
        return await get_pokemon(name)
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
