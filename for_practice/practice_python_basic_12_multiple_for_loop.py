# @Author: JayY
# @Date:   2018-11-07T13:25:45+09:00
# @Filename: practice_python_basic_12_multiple_for_loop.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T14:04:09+09:00
# @Copyright: JayY

# how to print multiple for loop at once

a = [1, 1, 1, 1, 1, 1, 1]
b = [2, 2, 2, 2, 2, 2, 2]
c = [3, 3, 3, 3, 3, 3, 3]
d = [4, 4, 4, 4, 4, 4]

# for i, j in list(map(None, a, d)):
#     print(i, j)

for i, j in zip(a, d):
    print(i, j)

# for i, j in map(None, a, d):
#     print(i, j)

# for i, j, k in map(None, a, b, c):
#      print(i, j, k)

for i, j, k in zip(a, b, c):
    print(i, j, k)

# print([(i, j, k) for i in range(10) for j in range(10) for k in range(10)])
#
# for (i, j, k) in [a, b, c]:
#     print(j)

# for (i, j, k) in (a, b, c):
#     print(i, j, k)

# for [i, j, k] in a, b, c:
#     print([i, j, k])

# for (i, j, k) in a, b, c:
#     print(i, j, k)
