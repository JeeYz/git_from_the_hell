# @Author: JayY
# @Date:   2018-09-11T15:06:33+09:00
# @Filename: new_25.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:29:09+09:00
# @Copyright: JayY

# new_25.py
# numpy random uniform
# =========================================

'''
# e.g. numpy random uniform
'''
import numpy as np

a = np.array(np.random.uniform(-1.0, 1.0, 300))
#print(type(a))
b = list(a)
#print(type(b))
#print(b)
c = dict()
c = {'c':[7, 8, 9], 'a':[1, 2, 3], 'b':[4, 5, 6]}
print(c)
print(c.keys(), c['a'], c.values())

c = dict(sorted(c.items()))
print(c, type(c))
