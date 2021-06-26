import json
import random


def get_all_quotes():
    with open("./data/quotes.json") as quotes:
        quotes = json.load(quotes)
    return quotes


def get_random_quote():
    return random.choice(get_all_quotes())


def get_quote_from_character(character: str):
    all_quotes = get_all_quotes()
    quotes = [i for i in all_quotes if i["character"] == character.capitalize()]
    return quotes or None
