"""
.. biblioteca:: Regresion lineal simple
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
# biblioteca que ya contiene nuestro regresor
from sklearn.linear_model import LinearRegression

#importar una metrica para comparar el error entre
#mis datos originales y mi prediccion
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
#1/n* sum((y_test[i] - y_pred[i])^2)



#leyendo nuestro conjunto de Datos
dataset = pd.read_csv('Salary_data.csv')
X = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values


#visualizacion de la variable independiente y la dependiente para ver
#la forma
plt.scatter(X, y, color="blue")
plt.title("Visualizando la relacion de las dos variables")
plt.xlabel("Anhos de experiencia")
plt.ylabel("Sueldo")
plt.show()


# 70% entrenamiento y 30% prueba
# 80% entrenamiento y 20% prueba
# X es la variable o variables independientes
# y es la variable dependiente
# train_test de forma aleatoria
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#train_test_split devuelve los vectores en formato
#fila y los algoritmos lo requieren en formato columna
# por eso es que aplicamos ese reshape
X_train = X_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)
#print(X_train) #[a b c d e f ...]
#print(X_train.reshape(-1, 1))
#[[a]
#[b]
#...
#]


regressor = LinearRegression()
# pasar los datos para entrenar - ese fit es para entrenar mi modelo
# con los datos de entrenamiento
regressor.fit(X_train, y_train)

# este es nuestro b_1
print(regressor.coef_)
# este es nuestro b_0
print(regressor.intercept_)

#Prediciendo nuestros valores
#estoy llamando a predict para predecir con mi modelo entrenado
# y le paso s'olo mis datos de prueba
# a partir del X_test mi modelo que ya fue entrenado
# calcula mi prediccion para y y lo estamos asignando a y_pred
y_pred = regressor.predict(X_test)


plt.scatter(y_test, y_pred, color="blue")
plt.title("Comparacion entre los datos original de test y los predichos")
plt.xlabel("Datos originales")
plt.ylabel("Prediccion")
plt.show()

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2score = r2_score(y_test, y_pred)
print("Mean squared error: "+str(mse))
print("Mean absolute error: "+str(mae))
print("R^2: " + str(r2score))

#un dato que no conozco
#y_new = regressor.predict(X_new)






#print(y_pred)
