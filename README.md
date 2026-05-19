# PokéExplorer

PokéExplorer is a Python exam project that allows users to explore Pokémon data through a web application.

The project uses a Streamlit frontend and a FastAPI backend. The backend fetches Pokémon data from PokeAPI, structures the data with Pydantic, performs statistics with Pandas and NumPy, and exposes API endpoints for the frontend. The application also includes an AI page where users can ask questions about a Pokémon using the OpenAI API.

## Get started

### Prerequisites

Before running the project, make sure you have installed:

- Python 3.11 or 3.12
- Docker Desktop
- Git

### Setup

1. Clone the project:

```bash
git clone <repository-url>
cd <project-folder>
```

2. Create a .env file in the project root. Use .env.example as a template

3. Start the project with Docker Compose: 
```bash
docker compose up --build
```

4. Stop the project with Docker Compose:
```bash
docker compose down
```

### Local development without Docker

1. Create and activate a virtual environment: 
```bash
python -m venv .venv
```

2. Start the virtual enviroment: 
```bash
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
python -m pip install -r backend/requirements.txt
python -m pip install -r frontend/requirements.txt
python -m pip install -r requirements-dev.txt
```

4. Start the backend: 
```bash
cd backend
python -m uvicorn app.main:app --reload --port 8001
```

5. Start the frontend in another terminal:
```bash
cd frontend
python -m streamlit run app.py
```

6. Run all tests and checks:
```bash
uv run pre-commit run --all-files
```

7. Or run them individually:
```bash
uv run pytest
uv run ruff check .
uv run ruff format .
uv run pyright
```

## Features

- Search for a Pokémon by name
- View Pokémon types, abilities, height, weight and base stats
- Compare multiple Pokémon visually
- Show statistics based on selected Pokémon
- Visualize data with Matplotlib
- Ask AI questions about a selected Pokémon
- Run tests and code quality checks
- Start the full application with Docker Compose

## API Endpoints
GET /health
GET /api/pokemon/{name}
GET /api/pokemon/compare?names=pikachu,charizard
GET /api/stats/summary?names=pikachu,charizard,bulbasaur
POST /api/ai/ask

## Technologies Used

### Frontend

- Streamlit
- Requests
- Pandas
- Matplotlib

### Backend

- FastAPI
- Pydantic
- HTTPX
- PokeAPI
- OpenAI API
- Python-dotenv

### Data and Statistics

- Pandas
- NumPy
- Matplotlib

### Testing and Code Quality

- pytest
- Ruff
- Pyright
- pre-commit
- uv

### Deployment / Runtime

- Docker
- Docker Compose