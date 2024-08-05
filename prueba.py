from db import load_films
from Film import Film


def main():
    peliculas = []
    for film in load_films()["result"]:
        peliculas.append(Film(film["properties"]["title"],
                         film["properties"]["episode_id"],
                         film["properties"]["release_date"],
                         film["properties"]["opening_crawl"],
                         film["properties"]["director"]))
        
    for pelicula in peliculas:
        pelicula.show()
    
    
main()