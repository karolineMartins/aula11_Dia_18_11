#

import pandas as pd 

df = pd.read_csv("ClassicDisco.csv")

#Filtrar musicas lençadas depois de 1980, mostre apenas
print(df[df["Year"] > 1980],[["Year", "Track"]])