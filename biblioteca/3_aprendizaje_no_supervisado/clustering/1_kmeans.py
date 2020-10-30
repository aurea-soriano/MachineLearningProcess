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


dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

plt.scatter(X[:,0], X[:,1], s=100, color="blue")
plt.grid()
plt.show()


kmeans = KMeans(n_clusters = 2,init="random", max_iter=300)

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



#forma empirica de calcular el numero de k
#n = len(X)
num_clusters = int(math.sqrt(len(X))/2)

print("Empirico"+str(num_clusters))



kmeans = KMeans(n_clusters = num_clusters,init="random", max_iter=300)

 # dentro de pred_y va a tener la lista de clusters resultantes
 # NOO es variable dependiente, es un atributo nuevo
 # son las etiquetas de cluster/grupo predichas
labels = kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1], s=100, c=labels)
plt.grid() # una opcion para mostrar nuestra malla grafica
#esta es la posicion de cada centroide en el grafico
# que no necesiramente esta asociado a un dato
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='red')
plt.title("K-means - M'etodo Emp'irico")
plt.show()



#inertia = suma de los cuadrados de las distancias de las muestras
#a su centroide m'as cercano CSS


#si es que usamos nuestro coeficiente de la silueta
# calculamos todos los coeficientes para cada distribucion
# de clusters y escogemos el que est'e m'as cerca de 1
css_vector = []

for i in range(2, 11):
    kmeans = KMeans(n_clusters = i, init = 'random')
    labels_tmp = kmeans.fit_predict(X)
    css_vector.append(kmeans.inertia_)
    print("number clusters ", i)
    print('SSE: ',kmeans.inertia_)
    print('Silhouette Score: ', metrics.silhouette_score(X, labels_tmp, metric='euclidean'))

plt.plot(range(2,11), css_vector)
plt.title("M'etodo del Codo - Elbow")
plt.xlabel("Numero de clases")
plt.ylabel('CSS')
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
plt.title("K-means - Con el resultado del metodo del codo")
plt.show()


# este es un indice externo que usa ys conocidos,
# pero como este no es el caso, no podemos usarla
from sklearn.metrics.cluster import normalized_mutual_info_score
print(normalized_mutual_info_score([0, 0, 1, 1], [0, 0, 1, 1]))
