"""
.. biblioteca:: Regresion lineal multiple
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
from sklearn.metrics import mean_squared_error
#1/n* sum((y_test[i] - y_pred[i])^2)


#importar nuestro conjunto de datos

dataset = pd.read_csv('50_Startups.csv')
dataset = pd.get_dummies(dataset, columns=["State"])


X = dataset.iloc[:, [0,1,2,4,5,6]].values
y = dataset.iloc[:,3].values

# 70% entrenamiento y 30% prueba
# 80% entrenamiento y 20% prueba
# X es la variable o variables independientes
# y es la variable dependiente
# train_test de forma aleatoria
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

regressor = LinearRegression()
regressor.fit(X_train,y_train)

print(regressor.coef_)
print(regressor.intercept_)

#Prediciendo nuestros valores
#estoy llamando a predict para predecir con mi modelo entrenado
# y le paso s'olo mis datos de prueba
# a partir del X_test mi modelo que ya fue entrenado
# calcula mi prediccion para y y lo estamos asignando a y_pred
y_pred = regressor.predict(X_test)


#estamos queriendo verificar que tan bien se ha ajustado
#nuestro modelo a los datos de entrenamiento
# si es que se ha ajustado bien el resultado deberia
#ser una linea perfecta
y_train_pred = regressor.predict(X_train)


plt.scatter(y_test, y_pred, color="blue")
plt.scatter(y_train, y_train_pred, color="red")
plt.title("Comparacion entre los datos original de test y los predichos")
plt.xlabel("Datos originales")
plt.ylabel("Prediccion")
plt.show()

mse = mean_squared_error(y_test, y_pred)
print("Imprimiendo nuestro error de prediccion: "+str(mse))
