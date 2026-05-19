from app.models.pokemon import PokemonResponse, PokemonStats
from app.services.pokeapi import parse_pokemon_response
from app.services.stats import create_stats_summary, pokemon_to_row


def create_test_pokemon(
    name: str,
    attack: int,
    defense: int,
    speed: int,
    total_stats: int,
) -> PokemonResponse:
    return PokemonResponse(
        name=name,
        types=["electric"],
        abilities=["static"],
        height=4,
        weight=60,
        stats=PokemonStats(
            hp=35,
            attack=attack,
            defense=defense,
            special_attack=50,
            special_defense=50,
            speed=speed,
        ),
        total_stats=total_stats,
    )


def test_parse_pokemon_response() -> None:
    fake_pokeapi_response = {
        "name": "pikachu",
        "types": [{"type": {"name": "electric"}}],
        "abilities": [
            {"ability": {"name": "static"}},
            {"ability": {"name": "lightning-rod"}},
        ],
        "height": 4,
        "weight": 60,
        "stats": [
            {"base_stat": 35, "stat": {"name": "hp"}},
            {"base_stat": 55, "stat": {"name": "attack"}},
            {"base_stat": 40, "stat": {"name": "defense"}},
            {"base_stat": 50, "stat": {"name": "special-attack"}},
            {"base_stat": 50, "stat": {"name": "special-defense"}},
            {"base_stat": 90, "stat": {"name": "speed"}},
        ],
    }

    pokemon = parse_pokemon_response(fake_pokeapi_response)

    assert pokemon.name == "pikachu"
    assert pokemon.types == ["electric"]
    assert pokemon.abilities == ["static", "lightning-rod"]
    assert pokemon.stats.attack == 55
    assert pokemon.stats.speed == 90
    assert pokemon.total_stats == 320


def test_pokemon_to_row() -> None:
    pokemon = create_test_pokemon(
        name="pikachu",
        attack=55,
        defense=40,
        speed=90,
        total_stats=320,
    )

    row = pokemon_to_row(pokemon)

    assert row["name"] == "pikachu"
    assert row["attack"] == 55
    assert row["defense"] == 40
    assert row["speed"] == 90
    assert row["total_stats"] == 320


def test_create_stats_summary() -> None:
    pokemon_list = [
        create_test_pokemon("pikachu", attack=55, defense=40, speed=90, total_stats=320),
        create_test_pokemon("charizard", attack=84, defense=78, speed=100, total_stats=534),
    ]

    summary = create_stats_summary(pokemon_list)

    assert summary["pokemon_count"] == 2
    assert summary["average_attack"] == 69.5
    assert summary["average_defense"] == 59.0
    assert summary["average_speed"] == 95.0
    assert summary["strongest_pokemon"] == "charizard"
    assert summary["fastest_pokemon"] == "charizard"
    assert summary["total_stats_by_pokemon"] == {
        "pikachu": 320,
        "charizard": 534,
    }
