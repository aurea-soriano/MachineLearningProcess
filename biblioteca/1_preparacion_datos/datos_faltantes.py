"""
.. biblioteca:: Preparacion de datos
   :plataforma: Unix, Windows, MAC
   :sinopsis: Tratamiento de Datos Faltantes
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>

"""

# Importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importando el conjunto de datos
dataset = pd.read_csv('ejemplo_datos.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Tratando valores faltantes
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
