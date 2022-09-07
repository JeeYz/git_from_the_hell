# @Author: J.Y.
# @Date:   2019-03-04T14:42:22+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-06T15:12:43+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import copy

for j,i in enumerate(reversed(range(10))):
    print(i, '\t', j)

print(j)
list1 = [1, 2, 3, 4, 5]
list2 = list()

list2 = copy.deepcopy(list1)

print(list2)

list3 = [1, 2, 3, 4]
list1.extend(list3)

print(list1)


print([i for i in range(1, 10)])
list4 = [i for i in range(9, 12)]
list1.extend(list4)
print(list1)

for i,j in enumerate([1, 2, 3], 2):
    print(i, '\t', j)

list5 = list()
list5.extend(list3)
print(list5)

list5.pop()
print(list5)









## endl
