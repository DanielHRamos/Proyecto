from db import load_films
from Film import Film
from Grafico import Grafico, Grafico2


def main():
    peliculas = []
    
    for film in load_films()["result"]:
        peliculas.append(Film(film["properties"]["title"],
                         film["properties"]["episode_id"],
                         film["properties"]["release_date"],
                         film["properties"]["opening_crawl"],
                         film["properties"]["director"]))
        

    
    while True:
        opcion = input(f"1. Mostrar peliculas.\n2. Mostrar grafico de personajes nacidos en cada planeta. \n3. Mostrar graficos de caracteristicas de naves.\n0. Salir.\n\n\n>>> ")
        
        if opcion == "1":
            for pelicula in peliculas:
                pelicula.show_attr()
        
        elif opcion == "2":
            graphic = Grafico(r"C:\Users\Daniel\Desktop\starwars\csv\characters.csv")
            graphic.mostrar_grafico()
            
        elif opcion == "3":
            graphic1 = Grafico2(r"C:\Users\Daniel\Desktop\starwars\csv\starships.csv")
            graphic1.mostrar_grafico()
            
        elif opcion == "0":
            print("Gracias por usar el programa, que la fuerza te acompañe.")
            break
        
        else:
            print("Error, ingrese una opcion valida.")
             
main()