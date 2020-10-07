"""
    :ejemplo: Precios de casas
    :plataforma: Unix, Windows, Mac
    :sinopsis: Ejemplo de exploracion a partir de datos relacionados
    a precios de casas en Estados Unidos.
    :autora: Aurea Soriano. aurea.soriano@ic.unicamp.br
"""

#importar los paquetes mas importantes

import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns

df = pd.read_csv("../../datasets/USA_Housing.csv")

#print(df.head())
#print(df.columns)

#visualizacion basica con seaborn (pairplots)
#sns.pairplot(df)
#plt.show()


#Distribucion de los Precios
#df['Price'].plot.hist(bins=25, figsize=(8,4))
#plt.show()


#df['Price'].plot.density()
#plt.show()

print(df.corr())

plt.figure(figsize=(10,7))
sns.heatmap(df.corr(), linewidths=2)
plt.show()
