# @Author: JayY
# @Date:   2018-08-28T09:59:07+09:00
# @Filename: new_20.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:32:34+09:00
# @Copyright: JayY

# new_20.py
# practice making matrix
# ===================================

import numpy as np

a = [i for i in range(10)]

print(type(a), a)



print(type(a), a)

b = np.array([i for i in range(9)])
print(type(b), b)

c = list()
print(type(c))
c = b
print(type(c), c)

b = b.reshape(3, 3)
print(type(b), b)

e = [i+1 for i in range(10)]
print(type(e), e)

f = np.reshape(e, [2, 5])
print(type(f), f)
