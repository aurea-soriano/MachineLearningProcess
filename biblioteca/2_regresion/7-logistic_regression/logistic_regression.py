"""
.. biblioteca:: Logistic Regression
   :plataforma: Unix, Windows, MAC
   :sinopsis: Regression
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""

'''
estos datos estan relacionados a una campanha de marketing directo
(llamadas telefonicas) de una institucion bancaria
El objetivo es predecir si un cliente se suscribir'a a un paquete ofertado
deposito a plazo
'''


#importando nuestras bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Para dividir nuestro conjunto de Datos
from sklearn.model_selection import train_test_split


#biblioteca de logistic regression
from sklearn.linear_model import LogisticRegression


# tecnica usada para hacer un oversampling (replicacion de instancias)
# de la clase minoritaria
from sklearn.utils import resample


from sklearn.preprocessing import StandardScaler



#importar una metrica para comparar el error entre
#mis datos originales y mi prediccion
from sklearn.metrics import mean_squared_error



#read csv file
df = pd.read_csv('banking.csv')

df = pd.get_dummies(df,columns = ['job','marital','education','default',
                                   'housing','loan','month',
                                   'day_of_week','poutcome'], drop_first = True)

print(df.head())
print(df.columns)

contact =({'cellular':0, 'telephone':1})
df['contact'] = df['contact'].map(contact)

##  resultados desbalanceados
no_sub  = len(df[df['y']==0])
sub     = len(df[df['y']==1])
percent_no_sub =  (no_sub/len(df['y'])) * 100
percent_sub =  (sub/len(df['y'])) * 100


print("Aceptaron ", percent_sub)
print("No aceptaron ", percent_no_sub)

X = df.loc[:, df.columns != 'y']
y = df.loc[:, df.columns == 'y']


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3)
log_regression = LogisticRegression()
log_regression.fit(X_train, y_train)


y_pred = log_regression.predict(X_test)


plt.scatter(y_test, y_pred, color="blue")
plt.title("Comparacion entre los datos original de test y los predichos")
plt.xlabel("Datos originales")
plt.ylabel("Prediccion")
plt.show()

mse = mean_squared_error(y_test, y_pred)
print("Imprimiendo nuestro error de prediccion: "+str(mse))


#retornando a nuestra forma anterior
X = pd.concat([X_train, y_train], axis=1)

'''
X = Xtrain|ytrain
'''
# estamos sacando todas las instancias que pertenecen a no subscripciones
X_no_sub = X[X['y']==0]

# estamos sacando todas las instancias con subscripcion
X_sub = X[X['y']==1]


#upsampling, incremento de instancias para la clase minoritaria
#len (X_no_sub) -> forzando a que nuestra clase minoritaria tenga la misma
#cantidad de muestreas
X_sub_upsampled = resample(X_sub, replace=True, n_samples = len(X_no_sub))



#combinar nuestro nuevo X_sub_upsampled con nuestro X_no_sub anterior
X_upsampled = pd.concat([X_no_sub, X_sub_upsampled])


X_train = X_upsampled.loc[:, X_upsampled.columns != 'y']
y_train = X_upsampled.loc[:, X_upsampled.columns == 'y']


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


log_regression = LogisticRegression()
log_regression.fit(X_train, y_train)



y_pred = log_regression.predict(X_test)


plt.scatter(y_test, y_pred, color="blue")
plt.title("Comparacion entre los datos original de test y los predichos")
plt.xlabel("Datos originales")
plt.ylabel("Prediccion")
plt.show()


mse = mean_squared_error(y_test, y_pred)
print("Imprimiendo nuestro error de prediccion: "+str(mse))
