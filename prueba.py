from db import load_films
from Film import Film
from Natalidad import Natalidad
from Nave import Nave
from Estadistica import Estadistica
from MisionesA import menu_principal

def main():
    peliculas = []
    
    for film in load_films()["result"]:
        peliculas.append(Film(film["properties"]["title"],
                         film["properties"]["episode_id"],
                         film["properties"]["release_date"],
                         film["properties"]["opening_crawl"],
                         film["properties"]["director"]))
        

    
    while True:
        opcion = input(f"\nBienvenido a la metropedia de Star Wars, seleccione una opcion para continuar.\n\n1) Mostrar lista de peliculas.\n2) Mostrar grafico de personajes nacidos en cada planeta. \n3) Mostrar graficos de caracteristicas de naves. \n4) Mostrar tabla de estadisticas sobre naves. \n5) Construir mision. \n0) Salir.\n\n\n>>> ")
        
        if opcion == "1":
            for pelicula in peliculas:
                pelicula.show_attr()
        
        elif opcion == "2":
            graphic = Natalidad("characters.csv")
            graphic.mostrar_grafico()
            
        elif opcion == "3":
            graphic1 = Nave("starships.csv")
            graphic1.mostrar_grafico()
        
        elif opcion == "4":
            tabla = Estadistica("starships.csv")
            tabla.mostrar_tabla()
            
        elif opcion == "5":
            menu_principal()
            
        elif opcion == "0":
            print("Gracias por usar el programa, que la fuerza te acompañe.")
            break
        
        else:
            print("Error, ingrese una opcion valida.")
             
main()