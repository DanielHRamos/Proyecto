import requests
#Planets, starships, Vehicles, People, Films and Species


def load_films():
    url = requests.get("https://www.swapi.tech/api/films/")
    return url.json()

def load_species():
    pass

def load_planets():
    pass

def load_people():
    pass

def load_starships():
    pass

def load_vehicles():
    pass