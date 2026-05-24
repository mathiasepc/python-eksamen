from app.models.pokemon import PokemonResponse, PokemonStats
from app.services.stats_service import create_stats_summary, pokemon_to_row


def create_test_pokemon(
    name: str,
    attack: int,
    defense: int,
    speed: int,
    hp: int = 35,
    special_attack: int = 50,
    special_defense: int = 50,
) -> PokemonResponse:
    return PokemonResponse(
        name=name,
        types=["electric"],
        abilities=["static"],
        height=4,
        weight=60,
        stats=PokemonStats(
            hp=hp,
            attack=attack,
            defense=defense,
            special_attack=special_attack,
            special_defense=special_defense,
            speed=speed,
        ),
    )


def test_pokemon_to_row() -> None:
    pokemon = create_test_pokemon(
        name="pikachu",
        attack=55,
        defense=40,
        speed=90,
    )

    row = pokemon_to_row(pokemon)

    assert row["name"] == "pikachu"
    assert row["hp"] == 35
    assert row["attack"] == 55
    assert row["defense"] == 40
    assert row["speed"] == 90
    assert row["special_attack"] == 50
    assert row["special_defense"] == 50


def test_create_stats_summary() -> None:
    pokemon_list = [
        create_test_pokemon(
            name="pikachu",
            attack=55,
            defense=40,
            speed=90,
            hp=35,
            special_attack=50,
            special_defense=50,
        ),
        create_test_pokemon(
            name="charizard",
            attack=84,
            defense=78,
            speed=100,
            hp=78,
            special_attack=109,
            special_defense=85,
        ),
    ]

    summary = create_stats_summary(pokemon_list)

    assert summary.pokemon_count == 2

    assert summary.max_attack.name == "Charizard"
    assert summary.max_attack.value == 84

    assert summary.max_speed.name == "Charizard"
    assert summary.max_speed.value == 100

    assert summary.max_hp.name == "Charizard"
    assert summary.max_hp.value == 78

    assert summary.max_defense.name == "Charizard"
    assert summary.max_defense.value == 78

    assert summary.max_special_attack.name == "Charizard"
    assert summary.max_special_attack.value == 109

    assert summary.max_special_defense.name == "Charizard"
    assert summary.max_special_defense.value == 85
