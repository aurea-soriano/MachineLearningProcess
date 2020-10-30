import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import pandas as pd


def myKmeans(data, k, maxIters, initMethod):
    """
    data : por ahora es solo 2 dimensiones :-).
    k : numero de clusters deseados.
    maxIters : numero maximo de iteraciones para parar el calculamos
    de los centroides si los centroides finales no son determinados
    (no convergen) en las iteraciones dadas.
    initMethod : implementaremos las dos estrategias
    para calcular los centroides iniciales: "aleatorio/random"
    y "kmeans++" (el m'etodo inteligente).
    """
    # numero de datos
    numInstances = data.shape[0]

    # numero de atributos
    numFeatures = data.shape[1]

    # generamos los centroides iniciales
    centroids = getInitCentroids(initMethod, k, data, numInstances, numFeatures)

    # Variables para contar las iteraciones
    # y para tener un registro de los centroides anteriores
    iterations = 0
    oldCentroids = np.empty(shape = [0, numFeatures])

    # pasos de kmeans
    while not shouldStop(oldCentroids, centroids, iterations, maxIters):
        iterations += 1
        oldCentroids = centroids

        # dando las etiquetas para cada punto basado en los centroides
        labels = getLabels(data, centroids)
        while set(labels) != set(range(k)) and iterations == 1:
            centroids = getInitCentroids(initMethod, k, data, numInstances,numFeatures)
            oldCentroids = centroids
            labels = getLabels(data, centroids)

        #asignar los centroides basados en las etiquetas de los puntos
        centroids = getNewCentroids(data, labels, k, numFeatures)
    return labels


# funcion para determinar la condicion
# de parada para iteraciones de cluster
def shouldStop(oldCentroids, centroids, iterations, maxIters):
    if iterations > maxIters:
        return True
    return np.array_equal(oldCentroids, centroids)


# funcion para actualizar las etiquepas de acuerdo a los centroides
def getLabels(data, centroids):
    labels = []
    for i in data:
        distances = np.sqrt(((centroids-i)**2).sum(axis=1))
        label = np.where(distances == min(distances))
        labels.append(label[0][0])
    return np.array(labels)


# funcion para obtener nuevos centroides
def getNewCentroids(data, labels, k, features):
    newCentroids= np.empty(shape = [0, features])
    for i in range(k):
        indices = np.where(labels == i)
        centroid = np.mean(data[indices[0], :], axis=0)
        newCentroids = np.vstack((newCentroids, centroid))
    return newCentroids




# funcion para iniciar los centroides, aqui implementaremos las dos formas
def getInitCentroids(method, k, d, data, features):
    if method == 'kmeans++':
        seeds = np.empty(shape = [0, features])

        # vamos a generar el primer centroide aleatorio
        firstSeedIndex = np.random.randint(0, data)
        firstSeed = d[firstSeedIndex]
        seeds = np.vstack((seeds, firstSeed))
        seedsIndexList = [firstSeedIndex]

        # vamos a calcular la distancia al cuadrado de todos los puntos
        # al primer punto centroide aleatorio
        distSeeds = ((d-firstSeed)**2).sum(axis=1)


        #vamos calcular la distancia acumulada
        # para todos los puntos los cuales actuan como pesoss
        # para la distribucion de probabilidad
        distCumulative = np.cumsum(distSeeds)


        # hora de calcular los siguientes K centroids :-)
        for _ in range(k - 1):
            # extrayendo la suma acumulada mas grande
            greatestCumVal = int(distCumulative[-1])

            # determinando el peso random a partir  la suma acumulada
            nextSeedRandWeight = np.random.randint(0, greatestCumVal)

            # determinando la proxima semilla baandonos en la probabilidad de distribucion
            nextSeedIndex = np.searchsorted(distCumulative, nextSeedRandWeight,
                                            side="left")
            nextSeed = d[nextSeedIndex]

            #  REpite las 3 instrucciones si la semilla ya existe
            while (nextSeedIndex in seedsIndexList):
                nextSeedRandWeight = np.random.randint(0, greatestCumVal)
                nextSeedIndex = np.searchsorted(distCumulative,
                                                nextSeedRandWeight, side="left")
                nextSeed = d[nextSeedIndex]
                print(seedsIndexList)
                print(nextSeedIndex)
            seedsIndexList.append(nextSeedIndex)

            # adicionando los nuevos centroides a las semillas
            seeds = np.vstack((seeds, nextSeed))

            # calculando las distancias al cuadrado de los puntos
            # al proximo centroide
            # (nextSeed).

            #distNextSeed = squareDistance(nextSeed, d)
            distNextSeed = ((d-nextSeed)**2).sum(axis=1)

            # adicionando las distancias a la variables distSeeds.
            distSeeds = np.vstack((distSeeds, distNextSeed))

            # vamos a determinar la distancia al cuadrado para cada punto
            #con relacion al centroide
            distNewSeeds = []
            for i in range(data):
                distNewSeeds.append(min(distSeeds[:,i]))
                distCumulative = np.cumsum(distNewSeeds)
    elif method == 'random':

        # columnas de la matriz semilla inicialmente representan las coordenadas del centroide
        seeds = np.empty(shape = [0, k])
        for i in range(features):
            values = []

            # Restringimos los valores aleatorios al rango de cada característica.
            minVal = min(d[:, i])
            maxVal = max(d[:, i])
            rangeVal = maxVal - minVal

            #Manejando características con rango cero, es decir, valores constantes.
            #imaginemos una caracteristica donde todas las instancias tengan el mismo
            #valor
            for j in range(k):
                if rangeVal != 0:
                    values.append(np.random.randint(minVal, maxVal) + np.random
                                  .random_sample())
                else:
                    values.append(float(minVal))
            #seeds.append(np.array(values))
            seeds = np.vstack((seeds, values))

        # Transposición de la matriz para que cada fila represente coordenadas de centroide.
        seeds = seeds.transpose()

    return seeds



dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

plt.scatter(X[:,0], X[:,1], s=100, color="blue")
plt.grid()
plt.show()



# Ejecutando nuestro Kmeans
my_labels = myKmeans(X, 5, 300, 'kmeans++')

plt.scatter(X[:,0], X[:,1], s=100, c=my_labels)
plt.grid() # una opcion para mostrar nuestra malla grafica
#esta es la posicion de cada centroide en el grafico
# que no necesiramente esta asociado a un datoplt.title("My kmeans")
plt.title("Mi Kmeans")
plt.show()




# Ejecutando el algoritmo de sklearn
kmeans_sklearn = KMeans(n_clusters=5, init='k-means++').fit(X)

plt.scatter(X[:,0], X[:,1], s=100, c=kmeans_sklearn.labels_)
plt.grid() # una opcion para mostrar nuestra malla grafica
#esta es la posicion de cada centroide en el grafico
# que no necesiramente esta asociado a un datoplt.title("My kmeans")
plt.title("Kmeans de sklearn")
plt.show()
