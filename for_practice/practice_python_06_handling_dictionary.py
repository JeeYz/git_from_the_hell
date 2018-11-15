# @Author: JayY
# @Date:   2018-10-02T08:40:32+09:00
# @Filename: new_33.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:39:20+09:00
# @Copyright: JayY

# new_33.py
# practice python
# handling dictionary
# ==============================================

'''
dictionary handling example && algorithm
'''
import copy

dict = {'a':[1, [2, 3, 4]], 'b':[5, [6, 7, 8]], 'c':[9, [2, 3, 4]]}
print(dict, len(dict), type(dict))
print(dict.keys())
print(dict.values())
print(dict.get('a'))
print(dict.get('a')[0])
print(dict.get('a')[1])

for i in dict.values():
    print(i, type(i))
    print(i[0], type(i[0]))
    print(i[1], type(i[1]))
for i in dict.items():
    print(i, type(i))

for i in dict.values():
    if i[1] == [2, 3, 4]:
        print(i[0])

list0 = [1, 2, 3, 4, 5, 6, 7]
for i in list0:
    print(i)

list1 = copy.deepcopy(list0[:-1])
print(list1)
