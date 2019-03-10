# @Author: JY
# @Date:   2019-02-13T11:22:32+09:00
# @Filename: e_23.py
# @Last modified by:   JY
# @Last modified time: 2019-02-20T10:15:42+09:00
# @Copyright: JeeY

import copy

list = [1, 2, 3, 4, 5, 6, 76]

list1 = copy.deepcopy(list[2:])

print(list[:-1])
print(list[2:])
print(list1)

for j,i in enumerate(reversed(list)):
    print(i)
    if j == 2:
        del list[-(2+1)]

print(list)





## endl
