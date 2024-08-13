import requests

class Especie:
    def __init__(self, data):
        self.name = data.get('name')
        self.height = data.get('average_height')
        self.classification = data.get('classification')
        self.homeworld = data.get('homeworld')
        self.language = data.get('language')
        self.people = data.get('people')
        self.films = data.get('films')

def get_species_data():
    url = 'https://www.swapi.tech/api/species/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        species_list = data.get('results', [])
        return species_list
    else:
        print(f"Error al obtener datos de SWAPI. Código de estado: {response.status_code}")
        return []

def mostrar_especies():
    species_list = get_species_data()
    species_objects = [Especie(species_data) for species_data in species_list]
    sorted_species = sorted(species_objects, key=lambda x: x.name)

    for species in sorted_species:
        print(f"Nombre: {species.name}")
        print(f"Altura: {species.height}")
        print(f"Clasificación: {species.classification}")
        print(f"Planeta de origen: {species.homeworld}")
        print(f"Lengua materna: {species.language}")
        print(f"Personajes: {', '.join(species.people)}")
        print(f"Episodios: {', '.join(species.films)}")
        print("-" * 40)

