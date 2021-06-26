import json


def update_quote(new_data: dict, filename="./data/quotes.json"):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


def update(quote, character):
    data = {
        "quote": quote,
        "character": character,
    }

    update_quote(data)
