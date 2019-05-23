# @Author: J.Y.
# @Date:   2019-04-08T02:53:18+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-23T13:29:00+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import numpy as np

def add_in_function(a, b):
    a = a - b
    return a

a = 10
b = 5
a = add_in_function(a,
b)

print(a)

for i,j in enumerate(range(10), 1):
    print("%d th %d \n" %(i,j))


c = np.array([1, 0, 5, 3, 4])
d = np.zeros([5, 6])
d[np.arange(5), c] = 1
print(d)
## endl
