"""
    :ejemplo: Incendio Forestal
    :plataforma: Unix, Windows, Mac
    :sinopsis: Ejemplo de exploracion a partir de datos relacionados
    a un incendio forestal en Portugal.
    (combinar datos metereologicos, con coordenadas X Y y tiempo)
    :autora: Aurea Soriano. aurea.soriano@ic.unicamp.br
"""

"""
X: coordenada espacial X en el mapa dado
Y: coordenada espacial Y en el mapa dado
month: el mes del incendio "jan", "dec"
day: el dia en el que se dio el Incendio "mon" "sun"

FWI -> indice metereologico de incendios
FFMC: humedad de combustible de la basura Forestal
DMC: humedad del combustible del material organico
DC: el nivel de sequia del suelo
ISI: componente de progapagacion
temp: temperatura en grados Celsius
RH: humedad relativa
wind: velocidad del viento
rain: lluvia
area: area quemada
"""

# incluyendo bibliotecas basicas

import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt


#cargando nuestro conjunto de datos
df = pd.read_csv("../../datasets/forestfires.csv")

#print("Imprimiendo la cabecera de nuestros datos")
#print(df.head())

#print("Imprimiendo las estadisticas principales de nuestros datos")
#print(df.describe())


#visualizando que area tiene una escala diferente (orden de magnitud)
#for i in df.describe().columns[:-2]:
#    df.plot.scatter(i,"area", grid=True)
#    plt.show()

#df.plot.scatter("X","area", grid=True)
#plt.show()

#print(np.log2(0+1))

#Problema! Area es tan grande que no nos permite ver el comportamiento
#real de nuestros datos
#truco: log2 de nuestros datos

#df['Log2-area'] = np.log2(df['area']+1)

#for i in df.describe().columns[:-2]:
#    df.plot.scatter(i,"Log2-area", grid=True)
#    plt.show()

#df.plot.scatter("X","Log2-area", grid=True)
#plt.show()


#truco: log10 de nuestros datos
#df['Log10-area'] = np.log10(df['area']+1)
#df.plot.scatter("X","Log10-area", grid=True)
#plt.show()


#Problema 2: tenemos datos nominales
# day - month en formato de texto

#print(df['month'])
#print(df['day'])


#Estrategia de conversion 1: usar funcion de pandas get_dummies

df2 = df.copy()
df2 = pd.get_dummies(df2) # convertir nuestros atributos
#nominales en columnas una por opcion
print(df2.columns)


#Estrategia de conversion 2: Codificar

from sklearn.preprocessing import LabelEncoder

df3 = df.copy()

#crear un objeto del tipo LabelEncoder
enc = LabelEncoder()
#LabelEncoder te presento mis datos de meses en formato de texto
enc.fit(df3['month'])
#print(df3['month'])
#transformame mi columna de mes a forma codificada
df3['month_encoded']= enc.transform(df3['month'])
#print(df3['month_encoded'])



#LabelEconder presento mis datos de dias en formato de texto
enc.fit(df3['day'])
#print(df3['day'])
#transformame mi columna de dia a forma codificada
df3['day_encoded']= enc.transform(df3['day'])
#print(df3['day_encoded'])


#Estrategia de conversion 3: Por posiciones (Medio-Manual)
df4 = df.copy()

months=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
days=["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

for i in range(0, len(df4["month"])):
    month_index = months.index(df4["month"][i]) + 1
    df4["month"][i] = month_index
    #print(df4["month"][i])

for i in range(0, len(df4["day"])):
    day_index = days.index(df4["day"][i]) + 1
    df4["day"][i] = day_index
    #print(df4["day"][i])


#Estrategia de conversion 4: eliminar esas columnas
df5 = df.copy()

# una forma de eliminar esas dos columnas
#df5 = df5.drop(["month","day"], axis=1) #1 para columna, 0 para fila

del df5["month"]
del df5["day"]
print(df5.head())
