import requests

def main():
    query = input("Introduce el nombre para buscar personajes: ")
    characters = SWAPI.search_characters(query)

    for character in characters:
        print(f"Nombre: {character.get('name')}")
        print(f"Planeta de origen: {SWAPI.get_planet_name(character.get('homeworld'))}")
        print(f"Títulos de episodios: {', '.join(SWAPI.get_film_titles(character.get('films')))}")
        print(f"Género: {character.get('gender')}")
        print(f"Especie: {character.get('species', ['Desconocida'])[0]}")
        # Agrega más información aquí (naves, vehículos, etc.)
        print("-" * 40)

if __name__ == "__main__":
    main()