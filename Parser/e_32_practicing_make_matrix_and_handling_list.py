# @Author: JeeY
# @Date:   2019-02-22T03:36:20+09:00
# @Last modified by:   JeeY
# @Last modified time: 2019-02-22T05:01:55+09:00
# @License: JY
# @Copyright: JY

import numpy as np

for i in range(10, 20):
    print(i)

list0 = [1, 2, 3, 4]
list1 = [5, 6, 7]
print(list0[:-1])
list0.extend(list1)
print(list0)

list2 = list()
list2.extend(list0)
list2.extend(list1)
print(list2)

list3 = np.full((10, 10), -3.0)
print(list3)

list4 = np.full(10, 1)
print(list4)

list5 = np.random.uniform(-1, 1, 20)
print(list5)


## endl
