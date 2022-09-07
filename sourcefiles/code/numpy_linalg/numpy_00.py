# -*- coding: utf-8 -*-

#%%

import numpy as np

import matplotlib.pyplot as plt


#%%

A = np.arange(10, 130, 10).reshape(3, 4)

B = np.arange(1, 5)


#%%
a = np.array([4, 3])

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.scatter(a[0], a[1], s=30)

ax.text(a[0]+0.2, a[1]+0.2, 'a', size=15)



