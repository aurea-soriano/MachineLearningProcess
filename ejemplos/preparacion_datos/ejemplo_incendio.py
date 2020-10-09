"""
.. ejemplo:: Incendio Forestal
   :plataforma: Unix, Windows, MAC
   :sinopsis: Ejemplo de Exploración a partir de datos relacionados a un incendio forestal en Portugal.
   (combinaremos datos metereológicos, espaciales y otros)
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>

"""
'''
X - coordenada espacial en X del mapa de la zona 1 a 9
Y - coordenada espacial en X del mapa de la zona 2 a 9

month - mes del año: "jan" to "dec"
day - día de la semana: "mon" to "sun"

Índice meteorológico de incendios (FWI)

FFMC - FFMC index from the FWI system: 18.7 to 96.20
El Código de Humedad de Combustible Fino (FFMC)
representa la humedad de combustible de los combustibles
de la basura forestal bajo la sombra de un dosel de bosque.

DMC - DMC index from the FWI system: 1.1 to 291.3
El Código de humedad Duff (DMC) representa la humedad del
combustible de material orgánico descompuesto debajo de la camada.

DC - DC index from the FWI system: 7.9 to 860.6
El Código de Sequía (DC) representa el nivel de sequía en el suelo.

ISI - ISI index from the FWI system: 0.0 to 56.10
El índice de propagación inicial (ISI) es análogo al
componente de propagación. Integra la humedad del
combustible para los combustibles muertos finos y la velocidad del
viento en la superficie para estimar un potencial de propagación.


temp - temperature in Celsius degrees: 2.2 to 33.30
RH - relative humidity in %: 15.0 to 100
wind - wind speed in km/h: 0.40 to 9.40
rain - outside rain in mm/m2 : 0.0 to 6.4
area - the burned area of the forest (in ha): 0.00 to 1090.84
'''

#incluyendo nuestras bibliotecas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../datasets/forestfires.csv')
print("Imprimiendo la cabecera de nuestros datos")
print(df.head())


#conoceremos nuestros datos
#Estadisticas básicas y visualización
print("Estadísticas básicas de nuestros datos")
print(df.describe())


#Area tiene una magnitud diferente
for i in df.describe().columns[:-2]:
    df.plot.scatter(i,'area',grid=True)
    #plt.show()


#Nuestra área no nos permite ver bien que pasa con los datos.
# truco log2 de nuestros datos!!

df['Log-area']=np.log2(df['area']+1)

for i in df.describe().columns[:-2]:
    df.plot.scatter(i,'Log-area',grid=True)
    #plt.show()


# Problema con los datos nominales

print(df['month'])
print(df['day'])

df.boxplot(column='Log-area',by='day')
#plt.show()

df.boxplot(column='Log-area',by='month')
#plt.show()


df2= pd.get_dummies(df)
print(df2.head())

#2da estrategia
from sklearn.preprocessing import LabelEncoder

df3 = df
#codificando nuestros meses
enc = LabelEncoder()
enc.fit(df3['month'])
print(enc.classes_)
df3['month_encoded']=enc.transform(df3['month'])

#imprimiendo nuestra nueva columna
print(df3.head())

#codificando nuestros días
enc.fit(df3['day'])
print(enc.classes_)
df3['day_encoded']=enc.transform(df3['day'])
print(df3.head(15))


#3era estrategia
df4 = df
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
days = ['mon','tue','thu','wed','fri','sat','sun']

for i in range(0, len(df4['month'])):
    month_index = months.index(df4['month'][i])
    day_index = days.index(df4['day'][i])
    df4['month_encoded'][i]= month_index
    df4['day_encoded'][i]= day_index
print(df4.head(15))

#4ta estrategia
df5 = df
#del df5['month']
#del df5['day']
df5 = df5.drop(['month', 'day'], axis = 1)
print(df5.head(15))
