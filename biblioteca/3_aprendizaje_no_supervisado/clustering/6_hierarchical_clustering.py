"""
.. biblioteca:: Clustering with hierarchical clustering
   :plataforma: Unix, Windows, MAC
   :sinopsis: Clustering
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
import pandas as pd
from sklearn.cluster import AgglomerativeClustering


#bottom - up - aglomerativo
#empieza con todos en un cluster
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.title('Dendrogram')
plt.xlabel('Clientes')
plt.ylabel(' Distancias')
plt.show()


hc = AgglomerativeClustering(n_clusters=5, affinity = 'euclidean', linkage = 'ward')
Y_hc = hc.fit_predict(X)
vis_clusters=hc.labels_



# Visualising the clusters
plt.scatter(X[vis_clusters == 0, 0], X[vis_clusters == 0, 1], s = 100, c = 'yellow', label = 'Cluster 1')
plt.scatter(X[vis_clusters == 1, 0], X[vis_clusters == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[vis_clusters == 2, 0], X[vis_clusters == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[vis_clusters == 3, 0], X[vis_clusters == 3, 1], s = 100, c = 'black', label = 'Cluster 4')
plt.scatter(X[vis_clusters == 4, 0], X[vis_clusters == 4, 1], s = 100, c = 'red', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
print()
