"""
.. biblioteca:: Recursive Feature Elimination (RFE)
   :plataforma: Unix, Windows, MAC
   :sinopsis: Feature Relevance
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""

## usando los datasets de sklearn para jalar ejemplos
from sklearn import datasets
#este es el paquete de nuestro RFE
from sklearn.feature_selection import RFE

#modelos de regresion
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor


#iris datasets
dataset = datasets.load_iris() # tiene 4 atributos

model = LogisticRegression()

#crear nuestro RFE model para seleccionar 3 atributos

rfe = RFE(model, 3)
rfe = rfe.fit(dataset.data, dataset.target)



# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)

#[False  True  True  True]
#[2 1 1 1]

rfe = RFE(estimator=DecisionTreeRegressor(), n_features_to_select=3)
rfe = rfe.fit(dataset.data, dataset.target)
print(rfe.support_)
print(rfe.ranking_)


#[ True False  True  True]
#[1 2 1 1]
