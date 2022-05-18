import json

import requests


API_BASE = "https://swapi.dev/api/"


def list_people() -> dict:
    response = requests.get(f"{API_BASE}people")
    return json.loads(response.text)


if __name__ == "__main__":
    print(list_people())
