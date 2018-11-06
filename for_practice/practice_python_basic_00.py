# @Author: JayY <JeeYz>
# @Date:   2018-11-01T11:51:33+09:00
# @Filename: practice_python_basic_00.py
# @Last modified by:   JeeYz
# @Last modified time: 2018-11-02T14:00:10+09:00
# @Copyright: JayY



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
