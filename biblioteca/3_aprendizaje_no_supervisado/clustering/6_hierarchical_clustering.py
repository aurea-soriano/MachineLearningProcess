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
from scipy.cluster.hierarchy import to_tree
import math
import matplotlib.patches as mpatches
from sklearn.preprocessing import StandardScaler
from scipy.spatial import ConvexHull
from matplotlib.patches import Polygon


#bottom - up - aglomerativo
#empieza con todos en un cluster
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values


X = StandardScaler().fit_transform(X)
plt.scatter(X[:,0], X[:,1], s = 100, color='blue') #posicionamento dos eixos x e y
plt.grid() #função que desenha a grade no nosso gráfico
plt.show()


dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.title('Dendrogram')
plt.xlabel('Clientes')
plt.ylabel(' Distancias')
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(8, 3))
dn1 = sch.dendrogram(sch.linkage(X, method="ward"), ax=axes[0], above_threshold_color='y',
                           orientation='top')
dn2 = sch.dendrogram(sch.linkage(X, method="ward"), ax=axes[1],
                           above_threshold_color='#bcbddc',
                           orientation='right')
plt.show()


hc = AgglomerativeClustering(n_clusters=5, affinity = 'euclidean', linkage = 'ward')
Y_hc = hc.fit_predict(X)
labels=hc.labels_


#visualizacion con circulos
max_label = np.max(labels)
means = []
radius = []
for i in range(0, max_label+1):
    points = []
    for j in range(0, len(X)):
        if labels[j] == i:
            points.append(X[j])
    mean = np.sum(np.array(points), axis=0)/len(points)
    means.append(mean)

    max_distance = math.sqrt(np.sum(pow(np.array(mean-points[0]),2)))

    for j in range(1, len(points)):
        distance = math.sqrt(np.sum(pow(np.array(mean-points[j]),2)))
        if distance > max_distance:
            max_distance = distance
    radius.append(max_distance*10000)



# Visualising the clusters
means = np.array(means)
radius = np.array(radius)
plt.scatter(means[:, 0], means[:, 1], s = radius, alpha=0.3, c = 'gray')
plt.scatter(X[labels == 0, 0], X[labels == 0, 1], s = 100, c = 'yellow', label = 'Cluster 1')
plt.scatter(X[labels == 1, 0], X[labels == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[labels == 2, 0], X[labels == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[labels == 3, 0], X[labels == 3, 1], s = 100, c = 'black', label = 'Cluster 4')
plt.scatter(X[labels == 4, 0], X[labels == 4, 1], s = 100, c = 'red', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
print()


# Visualising the clusters
means = np.array(means)
radius = np.array(radius)
plt.scatter(means[:, 0], means[:, 1], s = radius, alpha=0.3, c = 'gray')
plt.scatter(X[labels == 0, 0], X[labels == 0, 1], s = 100, c = 'yellow', label = 'Cluster 1')
plt.scatter(X[labels == 1, 0], X[labels == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[labels == 2, 0], X[labels == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[labels == 3, 0], X[labels == 3, 1], s = 100, c = 'black', label = 'Cluster 4')
plt.scatter(X[labels == 4, 0], X[labels == 4, 1], s = 100, c = 'red', label = 'Cluster 5')
axes = plt.gca()
axes.set_xlim([-5,5])
axes.set_ylim([-5,5])
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
print()



#visualizacion con convex hull (poligonos aproximados)
max_label = np.max(labels)
hulls = []
polys = []

for i in range(0, max_label+1):
    points = []
    for j in range(0, len(X)):
        if labels[j] == i:
            points.append(X[j])
    points = np.array(points)
    hull = ConvexHull(points)
    plt.plot(points[:,0], points[:,1], 'o')
    cent = np.mean(points, 0)
    pts = []
    for pt in points[hull.simplices]:
        pts.append(pt[0].tolist())
        pts.append(pt[1].tolist())

    pts.sort(key=lambda p: np.arctan2(p[1] - cent[1],
                                    p[0] - cent[0]))
    pts = pts[0::2]  # Deleting duplicates
    pts.insert(len(pts), pts[0])
    k = 1.1
    color = 'green'
    poly = Polygon(k*(np.array(pts)- cent) + cent,
                   facecolor=color, alpha=0.2)

    poly.set_capstyle('round')
    plt.gca().add_patch(poly)


plt.show()
