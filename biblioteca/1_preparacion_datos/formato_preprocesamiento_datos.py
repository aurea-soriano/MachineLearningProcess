"""
.. biblioteca:: Preparacion de datos
   :plataforma: Unix, Windows, MAC
   :sinopsis: Preparacion de datos
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>

"""
# Importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# Importando el conjunto de datos
dataset = pd.read_csv('ejemplo_datos.csv')

X = dataset.iloc[:, [0,1,2]].values
y = dataset.iloc[:, 3].values

# Conociendo nuestros Datos
print("*** conciendo nuestros datos***")
print("cabecera")
print(dataset.head())
print("descriptor de caracteristicas")
print(dataset.describe())
print("informacion sobre nulos y el tipo de objetos que hay en las columnas")
print(dataset.info())

# Verificando si hay datos faltantes
print("*** verificando si hay datos faltantes")
print(dataset.isnull().values.any())

# Verificando si hay nans
print("*** verificando si hay NaN (not a number)")
print(dataset.isnull().sum().sum())

# Estrategia para datos faltantes
#1era estrategia: reemplazar con 0 cada valor NaN de cada columna

#forma 1
dataset2 = dataset.copy()
dataset2['Age'] = dataset2['Age'].fillna(0)
dataset2['Salary'] = dataset2['Salary'].fillna(0)

#forma 2
dataset3 = dataset.copy()
dataset3['Age'] = dataset2['Age'].replace(np.nan, 0)
dataset3['Salary'] = dataset2['Salary'].replace(np.nan, 0)


#2da estrategia:reemplazar todas los valores NaN de todas las columnas

#forma 1
dataset4 = dataset.copy()
dataset4 =dataset4.fillna(0)


#forma 2
dataset5 = dataset.copy()
dataset5 = dataset5.replace(np.nan,0)


#3era estrategia: NaN usando la media de los vecinos

# biblioteca que nos hara ese calculo
from sklearn.impute import SimpleImputer


# obtenemos los valores
dataset6 = dataset.copy()

# creamos el imputer que es el que nos hara la magia
#otras estrategias que acepta imputer "mean", “median”, “most_frequent”,
#“constant” (pasandole una constante)
imr = SimpleImputer(missing_values=np.nan, strategy='mean')
imr = imr.fit(dataset6[['Age']])
dataset6['Age'] = imr.transform(dataset6[['Age']]).ravel()
imr = imr.fit(dataset6[['Salary']])
dataset6['Salary'] = imr.transform(dataset6[['Salary']]).ravel()



# Datos Categoricos
#Country y Purchased


#1era estrategia: get dummies

dataset7 = dataset6.copy()
dataset7= pd.get_dummies(dataset7)

#2da estrategia: manual
countries = ["France", "Spain", "Germany"]
purchased = ["No", "Yes"]

dataset8 = dataset6.copy()

for i in range(0, len(dataset8)):
    dataset8["Country"][i] = countries.index(dataset8["Country"][i])
    dataset8["Purchased"][i] = purchased.index(dataset8["Purchased"][i])


#3era estrategia: remover esas columnas

dataset9 = dataset6.copy()
#del dataset9['Country']
#del dataset9['Purchased']
dataset9 = dataset9.drop(['Country', 'Purchased'], axis = 1)




# Dividir el conjunto de datos en entrenamiento y prueba
print("dividiendo el conjunto de entrenamiento y prueba")
from sklearn.model_selection import train_test_split

l_column = list(dataset8.columns) # Making a list out of column names
len_feature = len(l_column) # Length of column vector list


#usaremos el dataset 8
X = dataset8[l_column[0:len_feature-1]]
y = dataset8[l_column[len_feature-1]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

print(X_train)
print(X_test)
