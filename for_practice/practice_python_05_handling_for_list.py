# @Author: JayY
# @Date:   2018-10-01T20:55:46+09:00
# @Filename: new_32.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:38:19+09:00
# @Copyright: JayY

# new_32.py
# practice python
# list and for function
# =====================================

'''
for / list examples
'''
for i in range(10, 0,-1):
    print(i)
for j in reversed(range(10)):
    print(j)
for i in range(2, 4):
    print(i)

a = [1, 2, 3]
b = [1, 2]
c = [1, 2, 3]

print(a==b)
print(a==c)
print(b==c)
print(a is b)
print(a is c)
print(b is c)
