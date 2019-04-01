# @Author: J.Y.
# @Date:   2019-03-14T09:56:12+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-01T09:58:33+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np
import time
import datetime
import sys
sys.path.append(r'./module/')
import keras_module_0 as k0

list0 = [1, 2, 3, 4, 5]
tup0 = tuple(list0)

print(tup0)
print(type(list0), type(tup0))

print(np.random.rand(3, 2))
print(np.random.uniform(-1.0, 1.0, (3, 4)))

for i in range(10000):
    print('Number : %d' % i, end='\r')
    # time.sleep(0.1)

print('\n')
for i in range(10, 20):
    print(i)


a = np.array([0, 1, 0])
print(a)
print(type(a))

print('\n\n')

print(datetime.datetime.now())
print('\n\n')

for i,j in enumerate(range(10), 1):
    print(i, j)

print('\n\n')

b = [i for i in range(1, 11)]
print(b, '\n')

c = list(b[:2])
d = list(b[2:])

print(c, '\n')
print(d, '\n')

print('\n\n')

e = c + d
print(e)


## endl
