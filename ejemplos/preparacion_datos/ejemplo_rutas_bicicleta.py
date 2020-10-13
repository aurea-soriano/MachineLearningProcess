"""
    :ejemplo: Rutas de Bicicleta
    :plataforma: Unix, Windows, Mac
    :sinopsis: Ejemplo de exploracion a partir de datos de rutas de bicicletas en Londres.
    :autora: Aurea Soriano. aurea.soriano@ic.unicamp.br
"""


from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

'''
funciones utiles
'''
# Grafos de Distribucion
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()

#correlacion
def plotCorrelationMatrix(df, graphWidth):
    filename = df.dataframeName
    df = df.dropna('columns') # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {filename}', fontsize=15)
    plt.show()


# Scatter and density plots
def plotScatterMatrix(df, plotSize, textSize):
    df = df.select_dtypes(include =[np.number]) # keep only numerical columns
    # Remove rows and columns that would lead to df being singular
    df = df.dropna('columns')
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    columnNames = list(df)
    if len(columnNames) > 10: # reduce the number of columns for matrix inversion of kernel density plots
        columnNames = columnNames[:10]
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k = 1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
    plt.suptitle('Scatter and Density Plot')
    plt.show()


##empezamos por journeys


nRowsRead = 1000 # coloca None si quieres leer todo
# journeys.csv tiene 1542844 filas en realidad,  pero nosotros solo estamos
#cargando las primeras 1000 filas
df1 = pd.read_csv('../../dataset/optimization/journeys.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'journeys.csv'
nRow, nCol = df1.shape
print(f'Hay {nRow} filas y {nCol} columnas')


print(df1.head(5))

#matriz de correlacion
plotCorrelationMatrix(df1, 8)


plotScatterMatrix(df1, 20, 10)


#ahora stations

nRowsRead = 1000 # coloca None si quieres leer todo
# stations.csv tiene 1542844 filas en realidad,  pero nosotros solo estamos
#cargando las primeras 1000 filas
df2 = pd.read_csv('../../dataset/optimization/stations.csv', delimiter=',', nrows = nRowsRead)
df2.dataframeName = 'stations.csv'
nRow, nCol = df2.shape
print(f'Hay {nRow} filas y {nCol} columnas')

print(df2.head(5))


plotCorrelationMatrix(df2, 8)

plotScatterMatrix(df2, 12, 10)


#Para mas visualizaciones geniales visita: https://edenau.github.io/visualize-bike-mobility/
