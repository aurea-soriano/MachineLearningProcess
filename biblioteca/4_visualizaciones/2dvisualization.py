import numpy as np
import matplotlib.pyplot as plt

data = np.array([[5., 30., 45., 22.],
  [5., 25., 50., 20.],
  [1.,  2.,  1.,  1.]])

color_list = ['b', 'g', 'r']

X = np.arange(data.shape[1])
for i in range(data.shape[0]):
  plt.bar(X, data[i],
    bottom = np.sum(data[:i], axis = 0),
    color = color_list[i % len(color_list)])

plt.show()
