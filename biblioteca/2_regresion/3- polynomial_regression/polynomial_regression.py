"""
.. biblioteca:: Regresion polinomial
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

#nuestra biblioteca que contiene la regresion polinomial
from sklearn.preprocessing import PolynomialFeatures

# biblioteca que ya contiene nuestro regresor
from sklearn.linear_model import LinearRegression

#importar nuestro conjunto de datos

dataset = pd.read_csv('50_Startups.csv')
dataset = pd.get_dummies(dataset, columns=["State"])


X = dataset.iloc[:, [0,1,2]].values #[0,1,2,4,5,6]].values
y = dataset.iloc[:,3].values

#creando nuestro modelo usando un grado 4
#  x^4

#print(X[1,:])
# aqui estamos convirtiendo nuestros X a una version polinomica de grado 4
poly_reg = PolynomialFeatures(degree=4)
# obteniendo  nuestra transformacion de los X a forma polinomica
X_poly = poly_reg.fit_transform(X)
#x^4+ .. +x^2 = y
poly_reg.fit(X_poly, y)
#print(X_poly[1,:])

linear_reg = LinearRegression()
linear_reg.fit(X_poly, y)

# 70% entrenamiento y 30% prueba
# 80% entrenamiento y 20% prueba
# X es la variable o variables independientes
# y es la variable dependiente
# train_test de forma aleatoria
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.3)


# obtenemos nuestra Prediccion
y_pred = linear_reg.predict(X_test)



plt.scatter(y_test, y_pred, color="blue")
plt.title("Comparacion entre los datos original de test y los predichos")
plt.xlabel("Datos originales")
plt.ylabel("Prediccion")
plt.show()

mse = mean_squared_error(y_test, y_pred)
print("Imprimiendo nuestro error de prediccion: "+str(mse))
