
# this file is just python practicing
# practicing for basic garammar of python
# ==============================================


import tensorflow as tf
import numpy as np

from numpy import *
random.rand(10, 2)

hello = tf.constant('hello, Tensorflow!')
sess = tf.Session()
print(sess.run(hello))

for i in range(10):
    print(i)


class Person():
    def __init__(self):
        print('hello, world')


a = Person()

b = (1, 2, 3, 4)

c = [num * 3 for num in b if num % 2 == 0]

print(c)

ans = 1.e-5

print(ans)

np.random.random()
