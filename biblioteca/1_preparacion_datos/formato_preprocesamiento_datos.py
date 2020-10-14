"""
.. biblioteca:: Preparacion de datos
   :plataforma: Unix, Windows, MAC
   :sinopsis: Preparacion de datos
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>

"""

#Importar las bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#biblioteca para interpolar datos faltantes
from sklearn.impute import SimpleImputer

# Para dividir nuestro conjunto de Datos
from sklearn.model_selection import train_test_split



#Leer nuestro conjunto de Datos
dataset = pd.read_csv('ejemplo_datos.csv')



X = dataset.iloc[:, [0,1,2]].values
y = dataset.iloc[:, 3].values

#print("Variables a ser usadas en la prediccion")
#print(X)

#print("Variable objetivo")
#print(y)

#Conocer nuestros Datos
#print("cabecera")
#print(dataset.head())


#print("descripcion de los datos")
#print(dataset.describe())


#print("verificar si hay datos nulos y que tipo de datos son")
#print(dataset.info())



#verificar si hay nulos (nan)
#print("verificar si hay NaN(not a number)")
#print(dataset.isnull().sum().sum())



#Estrategia para datos faltantes


#1era estrategia: reemplazar con 0 cada valor NaN de cada columna

#forma1
dataset2 = dataset.copy()
dataset2['Age'] = dataset2['Age'].fillna(0)
dataset2['Salary'] = dataset2['Salary'].fillna(0)

#print(dataset2)


#forma2
dataset3 = dataset.copy()
dataset3['Age'] = dataset3['Age'].replace(np.nan, 1000)
dataset3['Salary'] = dataset3['Salary'].replace(np.nan, 1000)


#print(dataset3)



#2da estrategia: reemplazar todos los valores NaN de todas las columnas
dataset4 = dataset.copy()
dataset4 = dataset4.fillna(0)
#print(dataset4)


dataset5 = dataset.copy()
dataset5 = dataset5.replace(np.nan, 1000)
#print(dataset5)


#3era estrategia: reemplazar los valores con estadisticas de los vecinos


dataset6 = dataset.copy()

# a crear nuestro objeto SimpleImputer
# strategies: mean, median, most_frequent, constant(una constante definida por
#el usuario)

imr = SimpleImputer(missing_values=np.nan, strategy='median')
imr = imr.fit(dataset6[['Age']])

#print(imr.transform(dataset6[['Age']]))
#print(imr.transform(dataset6[['Age']]).ravel())
dataset6['Age'] = imr.transform(dataset6[['Age']]).ravel()
#print(dataset6['Age'])


imr = imr.fit(dataset6[['Salary']])
dataset6['Salary'] = imr.transform(dataset6[['Salary']]).ravel()
#print(dataset6['Salary'])


# Limpiar, transformar nuestros datos categoricos
#Country y Purchased como texto (categoricos)


#1era estrategia: get dummies
dataset7 =  dataset6.copy()
dataset7 = pd.get_dummies(dataset7, columns=["Country"])
print(dataset7)
dataset7["Purchased_number"] = np.zeros(len(dataset7))

for i in range(0, len(dataset7)):
    if dataset7["Purchased"][i] ==  "Yes":
        dataset7["Purchased_number"][i] = 1
    else:
        dataset7["Purchased_number"][i] = 0

del dataset7["Purchased"]

print(dataset7)


#2da estrategia: hacerlo manualmente
dataset8 = dataset6.copy()

countries = ["France", "Spain", "Germany"]
purchased = ["No", "Yes"]


for i in range(0, len(dataset8)):
    dataset8["Country"][i] = countries.index(dataset8["Country"][i])
    dataset8["Purchased"][i] = purchased.index(dataset8["Purchased"][i])


#print(dataset8)


#3era estrategia: remover las columnas categoricas

dataset9 = dataset6.copy()
dataset9 = dataset9.drop(['Country', 'Purchased'], axis=1)
#print(dataset9)


#Ya tenemos nuestro conjunto limpio (dataset7)


#aprendizaje no supervisado
X = dataset7.iloc[:, [0,1,2,3,4,5]].values


#aprendizaje supervisado
# las variables que van a ser usadas en la prediccion (Regresion o clasificacion)
X = dataset7.iloc[:, [0,1,2,3,4]].values
#la variable a ser predicha
y = dataset7.iloc[:, 5].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(len(X_train))
print(len(X_test))
