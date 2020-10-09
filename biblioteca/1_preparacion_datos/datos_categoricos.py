"""
.. biblioteca:: Preparacion de datos
   :plataforma: Unix, Windows, MAC
   :sinopsis: Conversion de datos categoricos
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
dataset.describe()
dataset.info()

# Verificando si hay datos faltantes
dataset.isnull().values.any()

# Verificando si hay nams
dataset.isnull().sum().sum()

# Estrategia para datos faltantes
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Codificando categorica data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()


labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
