"""
.. biblioteca:: Preparacion de datos
   :plataforma: Unix, Windows, MAC
   :sinopsis: Formato de Preparacion de datos
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

# Dividir el conjunto de datos en entrenamiento y prueba
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Escalamiento de caracteristicas
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""
