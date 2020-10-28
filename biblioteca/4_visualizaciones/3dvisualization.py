from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
#To make a stacked 3d bar plot, you can
#accumulate your dz values and use them
#as the base for each next bar. Here's an example:
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim3d(0,10)
ax.set_ylim3d(0,10)

xpos = [2,5,8,2,5,8,2,5,8]
ypos = [1,1,1,5,5,5,9,9,9]
zpos = np.zeros(9)

dx = np.ones(9)
dy = np.ones(9)
dz = [np.random.random(9) for i in range(4)]  # the heights of the 4 bar sets

_zpos = zpos   # the starting zpos for each bar
colors = ['r', 'b', 'g', 'y']
for i in range(4):
    ax.bar3d(xpos, ypos, _zpos, dx, dy, dz[i], color=colors[i])
    _zpos += dz[i]    # add the height of each bar to know where to start the next

plt.gca().invert_xaxis()
plt.show()
