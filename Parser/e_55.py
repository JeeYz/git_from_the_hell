# @Author: J.Y.
# @Date:   2019-03-04T14:42:22+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-09T03:58:38+09:00
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

for i,j in enumerate(range(10), 1):
    print(i,j)

print(list1.index(5))

list6 = [1, 1, 2, 2, 2, 3, 3]
print(list6.index(3))
print(list6.count(3))
print(list6.count(2))

print('\n\n')

list8 = ['a', 'a', 'b', 'b', 'c', 'd', 'd', 'd']

for i,j in enumerate(list8, 1):
    print(i, ' ', j)

list7 = list()
for i,j in enumerate(list8, 1):
    j = str(j) + '__' + str(i)
    list7.append(j)

print(list7)
print(list8)











## endl
