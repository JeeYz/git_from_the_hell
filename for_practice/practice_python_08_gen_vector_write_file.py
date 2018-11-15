# @Author: JayY
# @Date:   2018-08-23T10:55:28+09:00
# @Filename: new_17.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:18:31+09:00
# @Copyright: JayY

# new_17.py
# generate vector and write to file

import numpy as np

#fp2 = open('example03.txt', 'r', encoding='utf-8')
#fp3 = open('example04.txt', 'w', encoding='utf-8')

'''
## *** NUMPY : the ways to create random numbers

a = np.random.rand(9).reshape(3, 3)
b = np.random.normal(0, 1, (3, 3))
c = np.random.random((3, 3))
d = np.random.uniform(0, 10, (3, 3))
#a = a.reshape(5, 5)

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
'''

def make_random_exam01():
    with open('example03.txt', 'w', encoding='utf-8') as fp1:
        for i in range(10):
            #a = str(np.random.rand(300))
            a = str(np.random.rand(300))
            a = a[1:-1]
            a = a.replace('\n', '')
            fp1.write(a + '\n')
    with open('example04.txt', 'w', encoding='utf-8') as fp1:
        for i in range(10):
            #a = str(np.random.rand(300))
            a = str(np.random.rand(300))
            a = a[1:-1]
            a = a.replace('\n', '')
            fp1.write(a + '\n')

make_random_exam01()
