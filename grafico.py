import pandas as pan
import matplotlib.pyplot as plot

class Grafico:
    def __init__(self, data):
        self.df = pan.read_csv(data)
        
    def pjs_por_planeta(self):
        return self.df["homeworld"].value_counts()
    
    def mostrar_grafico(self,figsize=(12,8)):
        # son 96 en total, pero el nro 19: Dron BB-8 tiene valor "None" en su carateristica
        # "homeworld" asi que el value_counts() no lo toma en cuenta.
        pjs = self.pjs_por_planeta()
        plot.figure(figsize=figsize)
        plot.bar(pjs.index, pjs.values)
        plot.xticks(rotation = 90)
        plot.title("Cantidad de personajes nacidos por planeta")
        plot.xlabel("Planeta")
        plot.ylabel("Numero de personajes")
        plot.show()

class Grafico2:
    def __init__(self, data):
        self.df =  pan.read_csv(data)
    def nombre_nave(self):
        return self.df["name"]
    
    def longitud_naves(self):
        return self.df["length"]
    
    def capacidad_carga(self):
        return self.df["cargo_capacity"]
    
    def clasif_hiper(self):
        return self.df["hyperdrive_rating"]
    
    def mglt(self):
        return self.df["MGLT"]
    
    def mostrar_grafico(self,figsize=(12,8)):
        # en este grafico hay 8 naves que tienen exactamente los mismos valores en cada atributo, por lo tanto
        # se omiten asi que de 60 naves que aparecen en el archivo cvs solo aparecen 52 en el grafico
        name = self.nombre_nave()
        
        long = self.longitud_naves()
        plot.figure(figsize=figsize)
        plot.title("Longitud de las naves")
        plot.bar(name.values, long.values)
        plot.xlabel("Naves")
        plot.ylabel("Longitud")
        plot.xticks(rotation=90)
        plot.show()
        
        
        cap = self.capacidad_carga()
        plot.figure(figsize=figsize)
        plot.title("Capacidad de carga de las naves")
        plot.bar(name.values,cap.values)
        plot.xlabel("Naves")
        plot.ylabel("Capacidad de carga (x10^8)")
        plot.xticks(rotation=90)
        plot.show()
        
        
        clas = self.clasif_hiper()
        plot.figure(figsize=figsize)
        plot.title("Clasificacion de hiperimpulsor")
        plot.bar(name.values, clas.values)
        plot.xlabel("Naves")
        plot.ylabel("Clasificacion")
        plot.xticks(rotation=90)
        plot.show()
        
        
        mglt = self.mglt()
        plot.figure(figsize=figsize)
        plot.title("Modern Galactic Light Time (MGLT)")
        plot.bar(name.values, mglt.values)
        plot.xlabel("Naves")
        plot.ylabel("MGLT")
        plot.xticks(rotation=90)
        plot.show()
        