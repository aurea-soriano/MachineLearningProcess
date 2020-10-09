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

#print(df.corr())

#plt.figure(figsize=(10,7))
#sns.heatmap(df.corr(), linewidths=2)
#plt.show()


#clasificacion
#cuales son las variables independientes que vamos a usar
#cual es la variable dependiente que vamos a categorizar o una variable que de por si
#sea categorizado
# caras #moderadas #economicas
# precio -> categorias  X> m1 (caro) m2<X<m3(moderado) X<m4(economico)


#Regresion -> estimar el precio cuanto costaria esa casa, considerando todas las
#caracteristicas dadas.
# todas las variables - direccion  -> precio

print(df.columns)

column_size = len(list(df.columns))
print(column_size)

# matriz nuestras variables numericas excepto el precio
X = df[df.columns[0:column_size-2]]
#lista para ser usada en los sgtes Parsonschester

# donde vamos a tener la variable objetivo
y = df[df.columns[column_size-2]]
#print(y)


#70% - 30% / 80%- 20%
