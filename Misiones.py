import csv
import os
from Mision import Mision

# Definimos las constantes para los archivos CSV
nombremision_CSV = 'Proyecto/battles.csv'
planeta_CSV = 'Proyecto/planets.csv'
nave_CSV = "Proyecto/starships.csv"
arma_CSV = 'Proyecto/weapons.csv'
personaje_CSV = 'Proyecto/characters.csv'

# Función para cargar los datos de los archivos CSV
def cargar_datos():
    battles = []
    planets = []
    starships = []
    weapons = []
    characters = []

    with open(nombremision_CSV, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            battles.append(row['name'])

    with open(planeta_CSV, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            planets.append(row['name'])

    with open(nave_CSV, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            starships.append(row['name'])

    with open(arma_CSV, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            weapons.append(row['name'])

    with open(personaje_CSV, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            characters.append(row['name'])

    return battles, planets, starships, weapons, characters

# Función para crear una misión
def crear_mision():
    battles, planets, starships, weapons, characters = cargar_datos() #REVISAR 
    print ()
    print("Seleccione el nombre de la misión:")
    for i, battle in enumerate(battles):
        print(f"{i+1}. {battle}")
    nombre = input("Ingrese el número de la misión: ")
    nombre = battles[int(nombre) - 1]
    print()
    print("Seleccione el planeta destino:")
    for i, planet in enumerate(planets):
        print(f"{i+1}. {planet}")
    print()
    planeta = input("Ingrese el número del planeta: ")
    planeta = planets[int(planeta) - 1]
    print()
    print("Seleccione la nave a utilizar:")
    for i, starship in enumerate(starships):
        print(f"{i+1}. {starship}")
    print()
    nave = input("Ingrese el número de la nave: ")
    nave = starships[int(nave) - 1]

    armas_seleccionadas = []
    print()
    print("Seleccione las armas a utilizar (hasta 7):")
    for i, weapon in enumerate(weapons):
        print(f"{i+1}. {weapon}")
    while len(armas_seleccionadas) < 7:
        arma = input("Ingrese el número de la arma (0 para terminar): ")
        if arma == "0":
            break
        armas_seleccionadas.append(weapons[int(arma) - 1])

    integrantes_seleccionados = []
    print()
    print("Seleccione los integrantes de la misión (hasta 7):")
    for i, character in enumerate(characters):
        print(f"{i+1}. {character}")
    while len(integrantes_seleccionados) < 7:
        integrante = input("Ingrese el número del integrante (0 para terminar): ")
        if integrante == "0":
            break
        integrantes_seleccionados.append(characters[int(integrante) - 1])

    mision = Mision(nombre, planeta, nave, armas_seleccionadas, integrantes_seleccionados)
    return mision

# Función para modificar una misión
def modificar_mision(misiones):
    print("Seleccione la misión a modificar:")
    for i, mision in enumerate(misiones):
        print(f"{i+1}. {mision.nombre}")
    seleccion = input("Ingrese el número de la misión: ")
    mision = misiones[int(seleccion) - 1]

    print("Seleccione el atributo a modificar:")
    print("1. Nombre")
    print("2. Planeta")
    print("3. Nave")
    print("4. Armas")
    print("5. Integrantes")
    atributo = input("Ingrese el número del atributo: ")

    if atributo == "1":
        mision.nombre = input("Ingrese el nuevo nombre: ")
    elif atributo == "2":
        battles, planets, starships, weapons, characters = cargar_datos()
        print("Seleccione el nuevo planeta destino:")
        for i, planet in enumerate(planets):
            print(f"{i+1}. {planet}")
        planeta = input("Ingrese el número del planeta: ")
        mision.planeta = planets[int(planeta) - 1]
    elif atributo == "3":
        battles, planets, starships, weapons, characters = cargar_datos()
        print("Seleccione la nueva nave a utilizar:")
        for i, starship in enumerate(starships):
            print(f"{i+1}. {starship}")
        nave = input("Ingrese el número de la nave: ")
        mision.nave = starships[int(nave) - 1]
    elif atributo == "4":
        battles, planets, starships, weapons, characters = cargar_datos()
        print("Seleccione las nuevas armas a utilizar (hasta 7):")
        for i, weapon in enumerate(weapons):
            print(f"{i+1}. {weapon}")
        mision.armas = []
        while len(mision.armas) < 7:
            arma = input("Ingrese el número de la arma (0 para terminar): ")
            if arma == "0":
                break
            mision.armas.append(weapons[int(arma) - 1])
    elif atributo == "5":
        battles, planets, starships, weapons, characters = cargar_datos()
        print("Seleccione los nuevos integrantes de la misión (hasta 7):")
        for i, character in enumerate(characters):
            print(f"{i+1}. {character}")
        mision.integrantes = []
        while len(mision.integrantes) < 7:
            integrante = input("Ingrese el número del integrante (0 para terminar): ")
            if integrante == "0":
                break
            mision.integrantes.append(characters[int(integrante) - 1])

#Función para visualizar una misión
def visualizar_mision(misiones):
    print ()
    print("Seleccione la misión a visualizar:")
    for i, mision in enumerate(misiones):
        print(f"{i+1}. {mision.nombre}")
    seleccion = input("Ingrese el número de la misión: ")
    mision = misiones[int(seleccion) - 1]

    print("Detalles de la misión:")
    print(f"Nombre: {mision.nombre}")
    print(f"Planeta destino: {mision.planeta}")
    print(f"Nave a utilizar: {mision.nave}")
    print("Armas a utilizar:")
    for arma in mision.armas:
        print(f"- {arma}")
    print("Integrantes de la misión:")
    for integrante in mision.integrantes:
        print(f"- {integrante}")

# Función para guardar misiones
def guardar_misiones(misiones):
    with open("misiones.txt", "w") as f:
        for mision in misiones:
            f.write(f"Nombre: {mision.nombre}\n")
            f.write(f"Planeta destino: {mision.planeta}\n")
            f.write(f"Nave a utilizar: {mision.nave}\n")
            f.write("Armas a utilizar:\n")
            for arma in mision.armas:
                f.write(f"- {arma}\n")
            f.write("Integrantes de la misión:\n")
            for integrante in mision.integrantes:
                f.write(f"- {integrante}\n")
            f.write("\n")

# Función para cargar misiones
def cargar_misiones(): #preguntar a Daniel 
    misiones = []
    if os.path.exists("misiones.txt"):
        with open("misiones.txt", "r") as f:
            lines = f.readlines()
            mision = {}
            for line in lines:
                if line.startswith("Nombre:"):
                    mision['nombre'] = line.strip().split(": ")[1]
                elif line.startswith("Planeta destino:"):
                    mision['planeta'] = line.strip().split(": ")[1]
                elif line.startswith("Nave a utilizar:"):
                    mision['nave'] = line.strip().split(": ")[1]
                elif line.startswith("Armas a utilizar:"):
                    mision['armas'] = []
                    while True:
                        line = next(f)
                        if line.strip() == "":
                            break
                        mision['armas'].append(line.strip().split("- ")[1])
                elif line.startswith("Integrantes de la misión:"):
                    mision['integrantes'] = []
                    while True:
                        line = next(f) 
                        if line.strip() == "":
                            break
                        mision['integrantes'].append(line.strip().split("- ")[1])
                if 'nombre' in mision and 'planeta' in mision and 'nave' in mision and 'armas' in mision and 'integrantes' in mision:
                    misiones.append(Mision(mision['nombre'], mision['planeta'], mision['nave'], mision['armas'], mision['integrantes']))
                    mision = {}
    return misiones

# Menú principal
def menu_principal():
    misiones = []
    while True:
        print()
        print('Bienvenidos al creador de misiones de Star Wars Metropedia')
        print ()
        print("Menú principal:")
        print("1. Crear misión")
        print("2. Modificar misión")
        print("3. Visualizar misión")
        print("4. Cargar misiones")
        print("5. Salir")
        opcion = input("Ingrese la opción que desea utilizar: ")

        if opcion == "1":
            if len(misiones) < 5:
                misiones.append(crear_mision())
            else:
                print("No se pueden crear más de 5 misiones.")
        elif opcion == "2":
            if len(misiones) > 0:
                modificar_mision(misiones)
            else:
                print("No hay misiones creadas.")
        elif opcion == "3":
            if len(misiones) > 0:
                visualizar_mision(misiones)
            else:
                print("No hay misiones creadas.")
        elif opcion == "4":
            misiones = cargar_misiones()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# ejecucion menú 
menu_principal()