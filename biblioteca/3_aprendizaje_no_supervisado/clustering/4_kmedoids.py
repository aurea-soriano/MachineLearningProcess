"""
.. biblioteca:: Clustering with Kmedoids/PAM
   :plataforma: Unix, Windows, MAC
   :sinopsis: Clustering
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn_extra.cluster import KMedoids
from sklearn.cluster import KMeans
import math
from sklearn import metrics


dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

plt.scatter(X[:,0], X[:,1], s=100, color="blue")
plt.grid()
plt.show()


kMedoids = KMedoids(n_clusters = 5, #numero de clusters
init = 'random',
max_iter = 300) #numero máximo de iteraciones
labels = kMedoids.fit_predict(X)
plt.scatter(X[:,0], X[:,1], s = 100,c = labels) #posicion de los ejes x y y
plt.grid() #funcion que grafica la malla
plt.scatter(kMedoids.cluster_centers_[:,0],kMedoids.cluster_centers_[:,1], s = 300, c = 'red') #posição de cada centroide no gráfico
plt.title("K-medoid")
plt.show()



#si es que usamos nuestro coeficiente de la silueta
# calculamos todos los coeficientes para cada distribucion
# de clusters y escogemos el que est'e m'as cerca de 1
css_vector = []

for i in range(2, 11):
    kMedoids = KMedoids(n_clusters = i, init = 'random')
    labels_tmp = kMedoids.fit_predict(X)
    css_vector.append(kMedoids.inertia_)
    print("number clusters ", i)
    print('SSE: ',kMedoids.inertia_)
    print('Silhouette Score: ', metrics.silhouette_score(X, labels_tmp, metric='euclidean'))

plt.plot(range(2,11), css_vector)
plt.title("M'etodo del Codo - Elbow")
plt.xlabel("Numero de clases")
plt.ylabel('CSS')
plt.show()

kMedoids = KMedoids(n_clusters = 6, #numero de clusters
init = 'random',
max_iter = 300) #numero máximo de iteraciones
labels = kMedoids.fit_predict(X)
plt.scatter(X[:,0], X[:,1], s = 100,c = labels) #posicion de los ejes x y y
plt.grid() #funcion que grafica la malla
plt.scatter(kMedoids.cluster_centers_[:,0],kMedoids.cluster_centers_[:,1], s = 300, c = 'red') #posição de cada centroide no gráfico
plt.title("K-medoid - metodo de elbow")
plt.show()


kMedoids = KMedoids(n_clusters = 7, #numero de clusters
init = 'random',
max_iter = 300) #numero máximo de iteraciones
labels = kMedoids.fit_predict(X)
plt.scatter(X[:,0], X[:,1], s = 100,c = labels) #posicion de los ejes x y y
plt.grid() #funcion que grafica la malla
plt.scatter(kMedoids.cluster_centers_[:,0],kMedoids.cluster_centers_[:,1], s = 300, c = 'red') #posição de cada centroide no gráfico
plt.title("K-medoid - cs")
plt.show()
