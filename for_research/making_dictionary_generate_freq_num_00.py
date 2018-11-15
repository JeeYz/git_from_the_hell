# @Author: JayY
# @Date:   2018-08-14T10:50:55+09:00
# @Filename: new_11.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T14:36:35+09:00
# @Copyright: JayY

# new_11.py

'''
# make dictionary list & making file of word dictionary
'''
import numpy as np
import time

fout = open("./data/korean_wiki/korean_wiki_result_words_00.txt", 'w', encoding='utf-8')

dic = dict()

with open("./data/korean_wiki/korean_wiki_temp_data_words.txt", 'r', encoding='utf-8') as f:
    while True:
        a = f.readline().split()
        if not a: break
        if a[0] in dic:
            dic[a[0]][1] += 1
            continue
        # change values
        dic[a[0]] = [a[1], ]
        # value is list type. so you can use append
        dic[a[0]].append(1)

dic = sorted(dic.items())
type(dic)
print(len(dic))

for tmp in dic:
    tmp = list(tmp)
    c1 = str(tmp[0])
    c2 = str(tmp[1][0])
    c3 = str(tmp[1][1])
    fout.write(c1 + '\t' + c2 + '\t' + c3 + '\n')

fout.close()
