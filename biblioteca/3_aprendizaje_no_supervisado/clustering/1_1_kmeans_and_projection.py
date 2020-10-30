"""
.. biblioteca:: Clustering with Kmeans
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
import umap
from sklearn.preprocessing import StandardScaler


dataset = pd.read_csv('Mall_Customers.csv')

#esto ya no podr'a ser visualizado  en 2D porque tiene 3 atributos
#entonces vamos a generar una proyecci'on 2D de estos datos

X = dataset.iloc[:, [2,3,4]].values

X = StandardScaler().fit_transform(X)

#vamos a usar una proyeccion llamada UMAP es
#reciente y mostr'o resultados buen'isimos
umap = umap.UMAP(n_neighbors=3,
                      min_dist=0.6,
                      metric='cosine')

#esta proyeccion solo va a ser usada para visualizaciones
#nuestro clustering ser'a hecho en el espacio ndimensional
#que en este caso n=3
X_projected = umap.fit_transform(X)

plt.scatter(X_projected[:,0], X_projected[:,1], s=100, color="blue")
plt.grid()
plt.show()


kmeans = KMeans(n_clusters = 7,init="random", max_iter=300)

 # dentro de pred_y va a tener la lista de clusters resultantes
 # NOO es variable dependiente, es un atributo nuevo
 # son las etiquetas de cluster/grupo predichas
labels = kmeans.fit_predict(X)
plt.scatter(X_projected[:,0], X_projected[:,1], s=100, c=labels)
plt.grid() # una opcion para mostrar nuestra malla grafica
#esta es la posicion de cada centroide en el grafico
# que no necesiramente esta asociado a un dato
plt.title("K-means con datos proyectados")
plt.show()
