from pydantic import BaseModel


class AskAIRequest(BaseModel):
    pokemon_name: str
    question: str


class AskAIResponse(BaseModel):
    pokemon_name: str
    question: str
    answer: str
