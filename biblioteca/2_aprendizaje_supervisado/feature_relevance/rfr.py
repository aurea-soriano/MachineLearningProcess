# random forest for feature importance on a regression problem
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot


X, y = make_regression(n_samples=1000, n_features=10, n_informative=5)

model = RandomForestRegressor()
model.fit(X, y)

importance = model.feature_importances_

print(importance)


for i, v in enumerate(importance):
    print("Feature ",i)
    print("Importance ",v)


pyplot.bar([x for x in range(len(importance))], importance)
pyplot.show()
