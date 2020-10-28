import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime,date
import calendar
from itertools import cycle, islice
#from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import numpy as np



dz=[]
z0 = np.array([ 31.,  23.,  11.,   8.,   7.,   6.,   6.,   6.,   5.,   4.,
                3.,   1.,   0.,  21.,  13.,  7.,   4.,   3.,   3.,   3.,
                3.,   1.,   0.,   0.,   0.,   0.,  22.,  11.,   4.,   2.,
                1.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,  38.,
                26.,  16.,  15.,   9.,   8.,  6.,   4.,   2.,   0.,   0.,
                0.,   0.,  47.,  26.,  21.,   11.,   9.,   7.,   6.,   4.,
                0.,   0.,   0.,   0.,   0.,  51.,  31.,  17.,  14.,   9.,
                6.,   5.,   0.,   0.,   0.,  0.,   0.,   0.,  33.,  25.,
                14.,   4.,   4.,   4.,   0.,   0.,   0.,   0.,   0.,   0.,
                0.,  35.,  24.,  14.,   9.,   5.,   0.,   0.,   0.,   0.,
                0.,   0.,   0.,   0.,  72.,  55.,  41.,  20.,   0.,   0.,
                0.,   0.,   0.,   0.,   0.,   0.,   0.,  50.,  27.,  15.,
                0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
                77.,  44.,   0.,   0.,   0.,  0.,   0.,   0.,   0.,   0.,
                0.,   0.,   0.,  82.])
dz.append(z0)

z1 =[ 14.,   5.,   8.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
      0.,   0.,  13.,   7.,   2.,   1.,   1.,   0.,   0.,   0.,   0.,
      0.,   0.,   0.,   0.,  14.,   8.,   4.,   0.,   1.,   0.,   0.,
      0.,   0.,   0.,   0.,   0.,   0.,  19.,   3.,   5.,   0.,   2.,
      0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,  11.,  13.,   3.,
      3.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,  19.,
      10.,   3.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
      0.,  13.,   2.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
      0.,   0.,   0.,  10.,   2.,   0.,   0.,   0.,   0.,   0.,   0.,
      0.,   0.,   0.,   0.,   0.,  11.,   1.,   3.,   0.,   0.,   0.,
      0.,   0.,   0.,   0.,   0.,   0.,   0.,  14.,   0.,   1.,   0.,
      0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,  12.,   3.,
      0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
      15.]

dz.append(z1)
_zpos = z0*0

xlabels = pd.Index(['01', '02', '03', '04', '05', '06', '07', '08', '09',
                    '10', '11', '12'], dtype='object', name='dates')

ylabels = pd.Index(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                    'Sep', 'Oct', 'Nov', 'Dec'], dtype='object',
name='Month')
x = np.arange(xlabels.shape[0])

y = np.arange(ylabels.shape[0])

x_M, y_M = np.meshgrid(x, y, copy=False)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

# Making the intervals in the axes match with their respective entries
ax.w_xaxis.set_ticks(x + 0.5/2.)
ax.w_yaxis.set_ticks(y + 0.5/2.)

# Renaming the ticks as they were before
ax.w_xaxis.set_ticklabels(xlabels)
ax.w_yaxis.set_ticklabels(ylabels)

# Labeling the 3 dimensions
ax.set_xlabel('Months Taken')
ax.set_ylabel('Month created')
ax.set_zlabel('Count')

# Choosing the range of values to be extended in the set colormap
values = np.linspace(0.2, 1., x_M.ravel().shape[0])

# Selecting an appropriate colormap

colors = ['#FFC04C', '#ee2f2f', '#3e9a19',
          '#599be5','#bf666f','#a235bf','#848381','#fb90d6','#fb9125']

for i in range(2):
    ax.bar3d(x_M.ravel(), y_M.ravel(), _zpos, dx=0.3, dy=0.3, dz=dz[i],
              color=colors[i])
    _zpos += dz[i]

#plt.gca().invert_xaxis()
#plt.gca().invert_yaxis()
Pending_proxy          = plt.Rectangle((0, 0), 1, 1, fc="#FFC04C90")
Declined_proxy         = plt.Rectangle((0, 0), 1, 1, fc="#ee2f2f90")

ax.legend([Pending_proxy,
           Declined_proxy],['Pending',
                            'Declined',
         ])
plt.show()
