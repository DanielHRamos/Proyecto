from db import load_films
from Film import Film
from Natalidad import Natalidad
from Nave import Nave
from Estadistica import Estadistica
from MisionesA import menu_principal
from Especie import mostrar_especies
from Planeta import mostrar_planeta
from Swapi import buscar_personaje
def main():
    peliculas = []
    
    for film in load_films()["result"]:
        peliculas.append(Film(film["properties"]["title"],
                         film["properties"]["episode_id"],
                         film["properties"]["release_date"],
                         film["properties"]["opening_crawl"],
                         film["properties"]["director"]))
        

    
    while True:
        opcion = input(f"\nBienvenido a la metropedia de Star Wars, seleccione una opcion para continuar.\n\n1) Mostrar lista de peliculas.\n2) Mostrar lista de las especies de seres vivos de la saga. \n3) Mostrar lista de planetas. \n4) Buscar personaje. \n5) Mostrar grafico de personajes nacidos en cada planeta. \n6) Mostrar graficos de caracteristicas de naves. \n7) Mostrar tabla de estadisticas sobre naves. \n8) Construir mision. \n0) Salir.\n\n\n>>> ")
        
        if opcion == "1":
            for pelicula in peliculas:
                pelicula.show_attr()
        
        elif opcion == "2":
            mostrar_especies()
            
        elif opcion == "3":
            mostrar_planeta()
            
        elif opcion == "4":
            buscar_personaje()
            
        elif opcion == "5":
            graphic = Natalidad("characters.csv")
            graphic.mostrar_grafico()
            
        elif opcion == "6":
            graphic1 = Nave("starships.csv")
            graphic1.mostrar_grafico()
        
        elif opcion == "7":
            tabla = Estadistica("starships.csv")
            tabla.mostrar_tabla()
            
        elif opcion == "8":
            menu_principal()
            
        elif opcion == "0":
            print("Gracias por usar el programa, que la fuerza te acompañe.")
            break
        
        else:
            print("Error, ingrese una opcion valida.")
             
main()