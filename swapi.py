import requests
class SWAPI:
    BASE_URL = 'https://www.swapi.tech/api/'

    @staticmethod
    def search_characters(query):
        url = f'{SWAPI.BASE_URL}people/?search={query}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('results', [])
        else:
            print(f"Error al obtener datos de SWAPI. Código de estado: {response.status_code}")
            return []

    @staticmethod
    def get_planet_name(url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('name', 'Desconocido')
        else:
            return 'Desconocido'

    @staticmethod
    def get_film_titles(film_urls):
        film_titles = []
        for film_url in film_urls:
            response = requests.get(film_url)
            if response.status_code == 200:
                film_data = response.json()
                film_titles.append(film_data.get('title'))
        return film_titles


def buscar_personaje():
    query = input("Introduce el nombre para buscar personajes: ")
    characters = SWAPI.search_characters(query)

    for character in characters:
        print(f"Nombre: {character.get('name')}")
        print(f"Planeta de origen: {SWAPI.get_planet_name(character.get('homeworld'))}")
        print(f"Títulos de episodios: {', '.join(SWAPI.get_film_titles(character.get('films')))}")
        print(f"Género: {character.get('gender')}")
        print(f"Especie: {character.get('species', ['Desconocida'])[0]}")
        print("-" * 40)