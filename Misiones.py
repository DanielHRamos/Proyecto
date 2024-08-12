import csv
import pandas
import numpy
 

# Clase Mision
class Mision:
    def __init__(self, nombre, planeta, nave, armas, integrantes):
        self.nombre = nombre
        self.planeta = planeta
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

# Clase SistemaMisiones
class SistemaMisiones:
    def __init__(self):
        self.misiones = []

    # Método para crear una misión
    def crear_mision(self):
        print("Crear misión:")
        nombre = input("Ingrese el nombre de la misión: ")
        planeta = self.seleccionar_planeta()
        nave = self.seleccionar_nave()
        armas = self.seleccionar_armas()
        integrantes = self.seleccionar_integrantes()
        mision = Mision(nombre, planeta, nave, armas, integrantes)
        self.misiones.append(mision)
        print("Misión creada con éxito!")

    # Método para seleccionar un planeta
    def seleccionar_planeta(self):
        print("Seleccione un planeta:")
        with open("planets.csv", "r") as f:
            reader = csv.reader(f)
            planetas = [row[0] for row in reader]
        for i, planeta in enumerate(planetas):
            print(f"{i+1}. {planeta}")
        seleccion = int(input("Ingrese el número del planeta: ")) - 1
        return planetas[seleccion]

    # Método para seleccionar una nave
    def seleccionar_nave(self):
        print("Seleccione una nave:")
        with open("starships.csv", "r") as f:
            reader = csv.reader(f)
            naves = [row[0] for row in reader]
        for i, nave in enumerate(naves):
            print(f"{i+1}. {nave}")
        seleccion = int(input("Ingrese el número de la nave: ")) - 1
        return naves[seleccion]

    # Método para seleccionar armas
    def seleccionar_armas(self):
        print("Seleccione armas (hasta 7):")
        with open("weapons.csv", "r") as f:
            reader = csv.reader(f)
            armas = [row[0] for row in reader]
        seleccionadas = []
        while len(seleccionadas) < 7:
            for i, arma in enumerate(armas):
                print(f"{i+1}. {arma}")
            seleccion = int(input("Ingrese el número del arma (0 para finalizar): ")) - 1
            if seleccion == -1:
                break
            seleccionadas.append(armas[seleccion])
        return seleccionadas

    # Método para seleccionar integrantes
    def seleccionar_integrantes(self):
        print("Seleccione integrantes (hasta 7):")
        with open("characters.csv", "r") as f:
            reader = csv.reader(f)
            integrantes = [row[0] for row in reader]
        seleccionados = []
        while len(seleccionados) < 7:
            for i, integrante in enumerate(integrantes):
                print(f"{i+1}. {integrante}")
            seleccion = int(input("Ingrese el número del integrante (0 para finalizar): ")) - 1
            if seleccion == -1:
                break
            seleccionados.append(integrantes[seleccion])
        return seleccionados

    # Método para modificar una misión
    def modificar_mision(self):
        if not self.misiones:
            print("No hay misiones definidas.")
            return
        print("Misiones definidas:")
        for i, mision in enumerate(self.misiones):
            print(f"{i+1}. {mision.nombre}")
        seleccion = int(input("Ingrese el número de la misión a editar: ")) - 1
        mision = self.misiones[seleccion]
        print("Editar misión:")
        print(f"Nombre: {mision.nombre}")
        print(f"Planeta: {mision.planeta}")
        print(f"Nave: {mision.nave}")
        print("Armas:")
        for i, arma in enumerate(mision.armas):
            print(f"{i+1}. {arma}")
        print("Integrantes:")
        for i, integrante in enumerate(mision.integrantes):
            print(f"{i+1}. {integrante}")
        while True:
            print("Opciones:")
            print("1. Agregar arma")
            print("2. Eliminar arma")
            print("3. Agregar integrante")
            print("4. Eliminar Integrante")