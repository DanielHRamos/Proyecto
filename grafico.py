import pandas as pan
import matplotlib.pyplot as plot

df = pan.read_csv(r"C:\Users\Daniel\Desktop\starwars\csv\characters.csv")


pjs_por_planeta = df["homeworld"].value_counts()
# son 96 en total, pero el nro 19: Dron BB-8 tiene valor "None" en su carateristica
# "homeworld" asi que el value_counts() no lo toma en cuenta.

plot.figure(figsize=(12,8))
plot.bar(pjs_por_planeta.index, pjs_por_planeta.values)
plot.xticks(rotation=90)
plot.title("Cantidad de personajes nacidos por planeta")
plot.xlabel("Planeta")
plot.ylabel("Numero de personajes")
plot.show()