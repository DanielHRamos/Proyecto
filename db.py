import requests


def load_films():
    url = requests.get("https://www.swapi.tech/api/films/")
    return url.json()