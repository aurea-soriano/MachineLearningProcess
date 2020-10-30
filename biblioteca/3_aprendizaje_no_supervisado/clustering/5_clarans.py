"""
.. biblioteca:: Clustering with Clarans
   :plataforma: Unix, Windows, MAC
   :sinopsis: Clustering
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""

from pyclustering.cluster.clarans import clarans;
from pyclustering.utils import timedcall;
import numpy as np #para manipular os vetores
from matplotlib import pyplot as plt #para plotar os gráficos
import pandas as pd
import math

# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values


"""!
The pyclustering library clarans implementation requires
list of lists as its input dataset.
Thus we convert the data from numpy array to list.
"""
data = X.tolist()

"""!
@brief Constructor of clustering algorithm CLARANS.
@details The higher the value of maxneighbor, the closer is CLARANS to K-Medoids, and the longer is each search of a local minima.
@param[in] data: Input data that is presented as list of points (objects), each point should be represented by list or tuple.
@param[in] number_clusters: amount of clusters that should be allocated.
@param[in] numlocal: the number of local minima obtained (amount of iterations for solving the problem).
@param[in] maxneighbor: the maximum number of neighbors examined.
"""
clarans_instance = clarans(data, 5, 6, 4);

#calls the clarans method 'process' to implement the algortihm
(ticks, result) = timedcall(clarans_instance.process);
print("Execution time : ", ticks, "\n");

#returns the clusters
clusters = clarans_instance.get_clusters();

#returns the mediods
medoids = clarans_instance.get_medoids();


vis_clusters = []

for i in range(0, len(X)):
    for j in range(len(clusters)):
        if i in clusters[j]:
            vis_clusters.append(j)

vis_clusters = np.array(vis_clusters)

print(medoids)

vis_medoids = []

for i in range(0, len(medoids)):
    vis_medoids.append(X[medoids[i]])

vis_medoids = np.array(vis_medoids)


# Visualising the clusters
plt.scatter(X[vis_clusters == 0, 0], X[vis_clusters == 0, 1], s = 100, c = 'yellow', label = 'Cluster 1')
plt.scatter(X[vis_clusters == 1, 0], X[vis_clusters == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[vis_clusters == 2, 0], X[vis_clusters == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[vis_clusters == 3, 0], X[vis_clusters == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[vis_clusters == 4, 0], X[vis_clusters == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(vis_medoids[:, 0], vis_medoids[:, 1], s = 300, c = 'red', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
