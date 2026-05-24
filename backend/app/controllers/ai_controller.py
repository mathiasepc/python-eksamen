from fastapi import APIRouter, HTTPException

from app.models.ai import AskAIRequest, AskAIResponse
from app.services.llm import ask_openai_about_pokemon
from app.services.pokeapi import get_pokemon

router = APIRouter(
    prefix="/api/ai",
    tags=["ai"],
)


@router.post("/ask", response_model=AskAIResponse)
async def ask_ai(request: AskAIRequest) -> AskAIResponse:
    if not request.pokemon_name.strip():
        raise HTTPException(status_code=400, detail="pokemon-name is required.")

    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question is required.")

    try:
        pokemon = await get_pokemon(request.pokemon_name)
        if not pokemon:
            raise HTTPException(status_code=404, detail=f"{pokemon} doesnt exist.")

        answer = ask_openai_about_pokemon(pokemon, request.question)

        return AskAIResponse(
            pokemon_name=pokemon.name,
            question=request.question,
            answer=answer,
        )

    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
