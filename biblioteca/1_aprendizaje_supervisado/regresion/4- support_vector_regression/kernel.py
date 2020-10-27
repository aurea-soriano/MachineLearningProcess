"""
.. biblioteca:: Exploration of kernels
   :plataforma: Unix, Windows, MAC
   :sinopsis: Kernels
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>
"""


#importing our libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([2,2,3,2,2,9,6,8,8,9])
labels = np.array([0,0,0,0,0,1,1,1,1,1])


fig = plt.figure()
ax  = fig.add_subplot(111)
plt.scatter(x, y, c=labels, s=60)
plt.plot([-2.5, 10], [12.5,-2.5], 'k-', lw=2)
ax.set_xlim([-5,15])
ax.set_ylim([-5,15])
plt.show()

x = np.array([1,1,2,3,3,6,6,6,9,9,10,11,12,13,16,18])
y = np.array([18,13,9,6,15,11,6,3,5,2,10,5,6,1,3,1])
labels = np.array([1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1])

fig = plt.figure()
ax  = fig.add_subplot(111)
plt.scatter(x, y, c=labels, s=60)
plt.show()



#our kernel function
def mapping(x,y):
    x = np.c_[(x, y)] # concatenando nuestros vectores en forma de columna
    if len(x)>2:
        x_1 = x[:,0]**2 # este era nuestro x
        x_2 = np.sqrt(2) * x[:,0] * x[:,1] ## \|2 * x * y
        x_3 = x[:,1]**2 # este era nuestro y
    else:
        x_1 = x[0]**2 # este era nuestro x
        x_2 = np.sqrt(2) * x[0] * x[1] ## \|2 * x * y
        x_3 = x[1]**2 # este era nuestro y
    trans_x = np.array([x_1, x_2, x_3])
    return trans_x


#x,y => x,y,z
trans_x = mapping(x,y)

fig = plt.figure()
ax  = fig.add_subplot(111, projection="3d")
ax.scatter(trans_x[0], trans_x[1], trans_x[2], c=labels, s=60)
ax.view_init(30, 185)
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')
plt.show()


fig = plt.figure()
ax  = fig.add_subplot(111, projection="3d")
ax.scatter(trans_x[0], trans_x[1], trans_x[1], c=labels, s=60)
ax.view_init(0, -180)
ax.set_zlim([-10000,10000])
ax.set_ylim([150,-50])
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')
plt.show()
