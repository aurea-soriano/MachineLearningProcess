"""
.. biblioteca:: Clustering with dbscan
   :plataforma: Unix, Windows, MAC
   :sinopsis: Clustering
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""

import numpy as np #para manipular os vetores
from matplotlib import pyplot as plt #para plotar os gráficos
from sklearn.cluster import DBSCAN
import pandas as pd
import math
from sklearn.preprocessing import StandardScaler



# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values


X = StandardScaler().fit_transform(X)
plt.scatter(X[:,0], X[:,1], s = 100, color='blue') #posicionamento dos eixos x e y
plt.grid() #função que desenha a grade no nosso gráfico
plt.show()

#eps
#
dbscan = DBSCAN(eps = 0.4, min_samples = 2, algorithm='kd_tree')

pred_y = dbscan.fit_predict(X)
max_label = np.max(pred_y)
plt.scatter(X[pred_y == -1, 0], X[pred_y == -1, 1], s = 100, c = 'gray', label = 'Anomalies')

for i in range(0, max_label+1):
    color = np.random.rand(3,)
    plt.scatter(X[pred_y == i, 0], X[pred_y == i, 1], s = 100, c = color, label = 'Cluster'+str(i))
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
