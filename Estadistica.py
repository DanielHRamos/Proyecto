import pandas as pan

class Estadistica:
    def __init__(self, data):
        self.df = pan.read_csv(data)
    
    def mostrar_tabla(self):
        agrupar_por_clase_nave = self.df.groupby("starship_class")
        costo = agrupar_por_clase_nave[["cost_in_credits"]].agg(["mean","median","min","max"])
        velocidad_max = agrupar_por_clase_nave[["max_atmosphering_speed"]].agg(["mean","median","min","max"])
        mglt = agrupar_por_clase_nave[["MGLT"]].agg(["mean","median","min","max"])
        hyperdrive_rating = agrupar_por_clase_nave[["hyperdrive_rating"]].agg(["mean","median","min","max"])

        print(costo,"\n\n\n\n",velocidad_max,"\n\n\n\n",mglt,"\n\n\n\n",hyperdrive_rating,"\n\n\n\n")    