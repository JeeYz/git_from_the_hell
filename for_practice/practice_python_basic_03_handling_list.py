# @Author: JayY
# @Date:   2018-09-21T12:03:10+09:00
# @Filename: new_29.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:35:28+09:00
# @Copyright: JayY

# new_29.py
# practice python basic
# handling list
# ======================================

with open('result_01.txt', 'r', encoding='utf-8') as f:
    a = f.readlines()
    b = list()
    for line in a:
        #print(line.split())
        b.append(line.split())
    print(b)
