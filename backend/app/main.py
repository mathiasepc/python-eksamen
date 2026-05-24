from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.ai_controller import router as ai_router

# route references
from app.controllers.pokemon_controller import router as pokemon_router
from app.controllers.stats_controller import router as stats_router

app = FastAPI(
    title="PokéExplorer API",
    description="Backend API for Pokémon data, statistics and AI features.",
    version="0.1.0",
)

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add our routes
app.include_router(pokemon_router)
app.include_router(stats_router)
app.include_router(ai_router)


# Just a check health check for my api.
@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
