import requests
from django.conf import settings
from django.db import IntegrityError

from characters.models import Character


def scrape_characters() -> list[Character]:
    url_to_scrape = settings.RICK_AND_MORTY_API_CHARACTERS_URL
    characters = []
    while url_to_scrape is not None:
        characters_response = requests.get(url_to_scrape).json()

        for characters_dict in characters_response["results"]:
            characters.append(
                Character(
                    api_id=characters_dict["id"],
                    name=characters_dict["name"],
                    status=characters_dict["status"],
                    species=characters_dict["species"],
                    gender=characters_dict["gender"],
                    image=characters_dict["image"],
                )
            )

        url_to_scrape = characters_response["info"]["next"]

    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        try:
            character.save()
        except IntegrityError:
            print(
                f"Character with 'api_id': {character.api_id} already exist in DB"
            )


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
