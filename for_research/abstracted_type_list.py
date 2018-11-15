# @Author: JayY
# @Date:   2018-10-19T12:15:46+09:00
# @Filename: abstract_type_list.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T16:54:28+09:00
# @Copyright: JayY


# making pos list for using sentence data files

fout = open('./data/types_abstracts.txt', 'w', encoding='utf-8')

with open('./data/type_abstracts.txt', 'r', encoding='utf-8') as f:
    while True:
        a = f.readline().split()
        if not a: break
        if int(a[1]) > 20:
            fout.write(a[0] + '\n')
