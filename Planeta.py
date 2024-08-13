import requests

class Planet:
    def __init__(self, data):
        self.name = data.get('name')
        self.orbital_period = data.get('orbital_period')
        self.rotation_period = data.get('rotation_period')
        self.population = data.get('population')
        self.climate = data.get('climate')


def get_planet_data():
    url = 'https://www.swapi.tech/api/planets/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        planet_list = data.get('results', [])
        return planet_list
    else:
        print(f"Error al obtener datos de SWAPI. Código de estado: {response.status_code}")
        return []

def mostrar_planeta():
    planet_list = get_planet_data()
    for planet_data in planet_list:
        planet = Planet(planet_data)
        print(f"Nombre: {planet.name}")
        print(f"Período de órbita: {planet.orbital_period}")
        print(f"Período de rotación: {planet.rotation_period}")
        print(f"Cantidad de habitantes: {planet.population}")
        print(f"Tipo de clima: {planet.climate}")


