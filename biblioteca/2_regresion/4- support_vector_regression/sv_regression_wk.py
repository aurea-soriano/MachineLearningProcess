"""
.. biblioteca:: Regresion SVR with kernels
   :plataforma: Unix, Windows, MAC
   :sinopsis: Regresion
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""
#importar nuestras bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Para dividir nuestro conjunto de Datos
from sklearn.model_selection import train_test_split

#importar una metrica para comparar el error entre
#mis datos originales y mi prediccion
from sklearn.metrics import mean_squared_error
#1/n* sum((y_test[i] - y_pred[i])^2)
