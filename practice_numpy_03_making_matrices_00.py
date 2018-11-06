# @Author: JayY
# @Date:   2018-09-19T10:46:34+09:00
# @Filename: new_27.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:30:25+09:00
# @Copyright: JayY

# new_27.py
# practice numpy nparray
# and making matrices
# ======================================

'''
practice for numpy and nparray
'''


import numpy as np
np.random.seed(1)
b = np.random.uniform(-1.0, 1.0, 30)

a = list(b)
print(a, type(a))

a = np.array(b)
print(a, type(a))

a = a.reshape(-1, 5)
print(a, type(a))

c = list()
for i in range(4):
    c.append(np.random.uniform(-1.0, 1.0, 30))

print(c, type(c))

c = np.array(c)
print(c, type(c))
c = c.reshape(-1, 5)
print(c, type(c))

for i in range(4):
    d = np.random.uniform(-1.0, 1.0, 30)
    a = np.concatenate((d, ))

print(a, type(a))
a = a.reshape(-1, 6)
print(a, type(a), a.shape)

'''
for i in range(4):
    d = np.random.uniform(-1.0, 1.0, 30)
    a = np.append(d)

print(a, type(a))
a =s a.reshape(-1, 6)
print(a, type(a), a.shape)
'''


for i in range(2):
    a = np.random.uniform(-1.0, 1.0, 30)
    #a = np.array(a)
    b = np.random.uniform(-1.0, 1.0, 30)
    #b = np.array(b)
    c = np.concatenate((a, b)).reshape(-1, 30)

print(a, type(a), a.shape)
print(b, type(b), a.shape)
print(c, type(c), c.shape)

b = list()
for i in range(4):
    d = np.random.uniform(-1.0, 1.0, 30)
    b.append(d)

print(b, type(b))
b = np.array(b).reshape(-1, 6)
print(b, type(b), b.shape)
