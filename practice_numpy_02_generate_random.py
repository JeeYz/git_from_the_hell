# @Author: JayY <JeeYz>
# @Date:   2018-10-30T09:36:58+09:00
# @Filename: practice_numpy_02_generate_random.py
# @Last modified by:   JeeYz
# @Last modified time: 2018-11-02T14:00:08+09:00
# @Copyright: JayY



# practice numpy again
# mainly, i had practiced for making random number with numpy library
# and practicing to multiply
# make dot product
# generate random matrix with several ways

import tensorflow as tf
import numpy as np

x = np.random.random((10, 10))
print(x)

x = np.random.randint(0.0, 10.0, (10, 10))
print(x)

x = np.random.randn(10, 10)
print(x)

a = np.array(range(10))
a.reshape(2, 5)
print(a)
print(len(a))
a = np.random.randint(0, 20, (2, 5))
print(a)

a = np.random.randint(0., 20., (2, 5))
print(a)

print(x)
y = np.random.random(10, )
print(y)
z = np.multiply(y, x)
print(z)

a = np.random.random_integers(-100, 100, 50)
print(a)


a = np.random.rand(100)
print(a)

a = np.random.randn(100)
print(a)

a = np.random.randn(10)
print(a)

print(a)

a = np.random.randn(10)
print(a)

mean = 0
std = 1
a = np.random.normal(mean, std, (3, 3))
print(a)

b = np.random.randint(0, 10, (3, 1))
print(b)
c = np.multiply(a, b)
print(c)

c = a*b
print(c)

d = np.random.random((3, 3))
print(d)

d = np.random.random((3, 4))
print(d)
e = d - 0.5
print(e)

print(a.shape)
print(b.shape)
print(c.shape)

f = np.dot(a, b)
print(f)
print(f.shape)
