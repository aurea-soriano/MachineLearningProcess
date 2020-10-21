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

#importar nuestro algoritmo
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler



#leer nuestro conjunto de Datos
dataset = pd.read_csv('50_Startups.csv')
dataset = pd.get_dummies(dataset, columns=["State"])

X = dataset.iloc[:, [0,1,2]].values #[0,1,2,4,5,6]].values
y = dataset.iloc[:,3].values

# 70% entrenamiento y 30% prueba
# 80% entrenamiento y 20% prueba
# X es la variable o variables independientes
# y es la variable dependiente
# train_test de forma aleatoria
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#linear, poly, rbf, sigmorid, precomputed
# C regularizacion 1.0
#epsilon 0.1 - 0.5 
sv_reg = make_pipeline(StandardScaler(), SVR(epsilon=0.2, kernel="poly"))
sv_reg.fit(X_train,y_train)

y_pred = sv_reg.predict(X_test)


plt.scatter(y_test, y_pred, color="blue")
plt.title("Comparacion entre los datos original de test y los predichos")
plt.xlabel("Datos originales")
plt.ylabel("Prediccion")
plt.show()
