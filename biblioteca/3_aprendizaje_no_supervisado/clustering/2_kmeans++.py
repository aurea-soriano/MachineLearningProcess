"""
.. biblioteca:: Clustering with Kmeans++
   :plataforma: Unix, Windows, MAC
   :sinopsis: Clustering
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import math
from sklearn import metrics


dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

plt.scatter(X[:,0], X[:,1], s=100, color="blue")
plt.grid()
plt.show()


kmeans = KMeans(n_clusters = 5,init="random", max_iter=300)
 # dentro de pred_y va a tener la lista de clusters resultantes
 # NOO es variable dependiente, es un atributo nuevo
 # son las etiquetas de cluster/grupo predichas
labels = kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1], s=100, c=labels)
plt.grid() # una opcion para mostrar nuestra malla grafica
#esta es la posicion de cada centroide en el grafico
# que no necesiramente esta asociado a un dato
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='red')
plt.title("K-means")
plt.show()



kmeansplus = KMeans(n_clusters = 5,init="k-means++", max_iter=300)
 # dentro de pred_y va a tener la lista de clusters resultantes
 # NOO es variable dependiente, es un atributo nuevo
 # son las etiquetas de cluster/grupo predichas
labels = kmeansplus.fit_predict(X)
plt.scatter(X[:,0], X[:,1], s=100, c=labels)
plt.grid() # una opcion para mostrar nuestra malla grafica
#esta es la posicion de cada centroide en el grafico
# que no necesiramente esta asociado a un dato
plt.scatter(kmeansplus.cluster_centers_[:,0], kmeansplus.cluster_centers_[:,1], s=300, c='red')
plt.title("K-means++")
plt.show()
