# @Author: JayY
# @Date:   2018-10-05T22:03:31+09:00
# @Filename: new_36.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:42:48+09:00
# @Copyright: JayY

# new_36.py
# practice numpy
# making matrix and handle it
# ========================================

import numpy as np
import random

a = [x for x in range(30)]
print(a, type(a))
a = np.array(a).reshape(-1, 3)
print(a, type(a), a.shape)

b = [x for x in range(20)]
c = [x for x in range(20)]
b += c
print(b, type(b))
b = np.array(b).reshape(-1, 5)
print(b, type(b))

b = [x for x in range(20)]
c = [x for x in range(20)]

b = np.concatenate((b, c)).reshape(-1, 20)
print(b, type(b))
