# @Author: JayY
# @Date:   2018-10-12T15:28:50+09:00
# @Filename: new_38.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:46:22+09:00
# @Copyright: JayY

# new_38.py
# practice numpy 
# ========================================

import numpy as np

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(a)
a.pop()
print(a)
a.insert(0,[3, 4, 5])
print(a)
b = a.pop()
print(a)
print(b)

a = [x for x in range(5)]
a = np.array(a).reshape((-1, 1))
print(a, type(a), a.shape)

'''
with open('train_skip_01_result.txt', 'r', encoding='utf-8') as f:
    data = list()
    while True:
        line = f.readline()
        if not line: break
        data.insert(0, line.split())
'''
'''
with open('train_skip_01_result.txt', 'r', encoding='utf-8') as f:
    data = f.read().split()
    data.reverse()
print(data)
'''
