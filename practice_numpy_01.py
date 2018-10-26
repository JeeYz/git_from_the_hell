# This file is for practicing numpy functions
# just practice

import numpy as np
# make zeros & ones
a = np.zeros((2, 2))
print(a)
b = np.ones((2, 3))
print(b)

c = np.full((2, 3), 5)
print(c)

d = np.eye(3)
print(d)

e = np.array(range(20)).reshape((4, 5))
print(e)

f = e[1:, 1:]
print(f)

g = e.reshape(20, )
print(g)

h = g.reshape(2, 10)
print(h)
