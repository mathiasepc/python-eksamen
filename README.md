PokéExplorer — teknisk kravspecifikation

Formål:
At udvikle en webapplikation i Python, hvor brugeren kan søge, sammenligne og analysere Pokémon-data 
samt stille spørgsmål til en AI-assistent.

Funktionelle krav
1. Søg Pokémon

Brugeren skal kunne indtaste navnet på en Pokémon og få vist:

Navn
Type(r)
Evner
Højde
Vægt
Base stats:
- HP
- Attack
- Defense
- Special Attack
- Special Defense
- Speed

2. Sammenlign Pokémon

Brugeren skal kunne vælge 2-4 Pokémon og sammenligne deres base stats visuelt med Matplotlib.

Eksempel på graf:

bar chart
radar-lignende graf
total stats sammenligning

3. Statistikside

Appen skal vise simple analyser baseret på Pandas/Numpy:

Gennemsnitlig attack pr. type
Gennemsnitlig defense pr. type
Pokémon med højest total stats
Normaliserede stats

4. AI-side

Brugeren skal kunne vælge en Pokémon og stille et spørgsmål.

Eksempel:

"Hvorfor er Charizard god offensivt?"

Backend sender Pokémon-data som kontekst til en LLM OpenAI.

5. Backend API

FastAPI skal stå for:

Hente data fra PokeAPI
Validere input
Strukturere responsdata
Levere data til Streamlit
Kalde LLM API

6. Tests og kodekvalitet

Projektet skal have:

pytest
type hints
mypy
ruff
unit tests

Minimum tests:

test_total_stats()
test_normalize_stats()
test_parse_pokemon_response()
test_invalid_pokemon_name()

7. Docker Compose

Projektet skal kunne startes med: docker compose up --build
Projektet skal kunne stoppes med: docker compose down

Teknisk arkitektur
Streamlit frontend
        |
        v
FastAPI backend
        |
        v
PokeAPI + LLM API

Frontend kommunikerer kun med backend. Det gør arkitekturen nemmere at forklare til eksamen, fordi du kan sige:

Streamlit håndterer præsentation og brugerinput, mens FastAPI håndterer datalogik, validering og eksterne API-kald.