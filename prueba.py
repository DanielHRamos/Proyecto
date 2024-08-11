from db import load_films
from Film import Film
from Natalidad import Natalidad
from Nave import Nave
from Estadistica import Estadistica


def main():
    peliculas = []
    prueba = 1
    for film in load_films()["result"]:
        peliculas.append(Film(film["properties"]["title"],
                         film["properties"]["episode_id"],
                         film["properties"]["release_date"],
                         film["properties"]["opening_crawl"],
                         film["properties"]["director"]))
        

    
    while True:
        opcion = input(f"\n1) Mostrar lista de peliculas.\n2) Mostrar grafico de personajes nacidos en cada planeta. \n3) Mostrar graficos de caracteristicas de naves. \n4) Mostrar tabla de estadisticas sobre naves. \n0) Salir.\n\n\n>>> ")
        
        if opcion == "1":
            for pelicula in peliculas:
                pelicula.show_attr()
        
        elif opcion == "2":
            graphic = Natalidad(r"C:\Users\Daniel\Desktop\Proyecto\Proyecto\characters.csv")
            graphic.mostrar_grafico()
            
        elif opcion == "3":
            graphic1 = Nave(r"C:\Users\Daniel\Desktop\Proyecto\Proyecto\starships.csv")
            graphic1.mostrar_grafico()
        
        elif opcion == "4":
            tabla = Estadistica(r"C:\Users\Daniel\Desktop\Proyecto\Proyecto\starships.csv")
            tabla.mostrar_tabla()
            
        elif opcion == "0":
            print("Gracias por usar el programa, que la fuerza te acompañe.")
            break
        
        else:
            print("Error, ingrese una opcion valida.")
             
main()