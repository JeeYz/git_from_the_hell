# @Author: JayY
# @Date:   2018-09-20T17:21:31+09:00
# @Filename: new_28.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:33:18+09:00
# @Copyright: JayY

# new_28.py
# practice python
# counting particular word that i choose
# ==================================

'''
counting particular word
'''


with open('result_07.txt', 'r', encoding='utf-8') as f:
    a = f.read()
    b = a.split()
    for i in b:
        if b.count(i) is 2:
            print(i)
