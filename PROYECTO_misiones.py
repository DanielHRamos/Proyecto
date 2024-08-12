import requests
import csv
import json


# Clase principal, aspectos dela  misión
class Mision:
    def __init__(self, nombre, planeta, nave, armas, integrantes):
        self.nombre = nombre
        self.planeta = planeta
        self.nave = nave
        self.armas = armas if armas else [] #REVISAR
        self.integrantes = integrantes if integrantes else []  #REVISAR######################

    def agregar_arma(self, arma):
        if len(self.armas) < 7:
            self.armas.append(arma)
        else:
            print("No se pueden agregar más de 7 armas.") #REVISAR

    def remover_arma(self, arma):
        if arma in self.armas:
            self.armas.remove(arma)

    def agregar_integrante(self, integrante):
        if len(self.integrantes) < 7:
            self.integrantes.append(integrante)
        else:
            print("No se pueden agregar más de 7 integrantes.")

    def remover_integrante(self, integrante):
        if integrante in self.integrantes:
            self.integrantes.remove(integrante)

    def mostrar_detalles(self):
        return {
            'nombre': self.nombre,
            'planeta': self.planeta,
            'nave': self.nave,
            'armas': self.armas,
            'integrantes': self.integrantes
        }

# Clase para gestionar las misiones
class GestorMisiones:
    def __init__(self):
        self.misiones = []

    def agregar_mision(self, mision): #ERROR 
        if len(self.misiones) < 5:
            self.misiones.append(mision)
        else:
            raise Exception("No se pueden agregar más de 5 misiones.")

    def listar_misiones(self):
        for i, mision in enumerate(self.misiones):
            print(f"{i + 1}. {mision.nombre}")

    def obtener_mision(self, indice):
        return self.misiones[indice]


#VIDEO 3 PROBAR
    def guardar_misiones(self, archivo):
        with open(archivo, 'w') as f:
            json.dump([mision.mostrar_detalles() for mision in self.misiones], f)

    def cargar_misiones(self, archivo):
        with open(archivo, 'r') as f:
            misiones_leidas = json.load(f)
            for mision_data in misiones_leidas:
                mision = Mision(**mision_data)
                self.agregar_mision(mision)
                
                
                