# @Author: JayY
# @Date:   2018-10-10T15:08:40+09:00
# @Filename: new_37.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:44:28+09:00
# @Copyright: JayY

# new_37.py
# practice numpy
# make matrices and calculate them in several ways
# ============================================

import numpy as np

a = np.array([x for x in range(10)]).reshape(-1, 5)
b = np.array([x for x in range(10)]).reshape(-1, 5)

c = np.matmul(a, np.transpose(b))
print(c)

c = np.tensordot(a, np.transpose(b), axes=0)
print(c, c.shape)

c = np.tensordot(a, np.transpose(b), axes=1)
print(c, c.shape)

c = np.tensordot(a, np.transpose(b), axes=([1, 0], [0, 1]))
print(c, c.shape)

a = np.arange(60.).reshape(3, 4, 5)
print(a, type(a), a.shape)
b = np.arange(24.).reshape(4, 3, 2)
print(b, type(b), b.shape)
c = np.tensordot(a, b, axes=([1, 0], [0, 1]))
print(c, type(c), c.shape)

a = np.arange(12.).reshape(3, 4)
print(a, type(a), a.shape)
b = np.arange(12.).reshape(4, 3)
print(b, type(b), b.shape)
c = np.tensordot(a, b, axes=([1, 0], [0, 1]))
print(c, type(c), c.shape)
c = np.dot(a, b)
print(c, type(c), c.shape)


a = np.arange(24).reshape((2,3,4))
print(a)
b = np.arange(4)
print(b)
print(np.inner(a, b))

a = np.array([x for x in range(16)]).reshape(4, 4)
print(a, type(a), a.shape)

b = list()
for i in range(4):
    for j in range(4):
        if i==j:
            b.append(a[i, j])

print(b, type(b))
