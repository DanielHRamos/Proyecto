import pandas as pan
import matplotlib.pyplot as plot

class Natalidad:
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