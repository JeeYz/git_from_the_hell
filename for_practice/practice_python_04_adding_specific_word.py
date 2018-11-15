# @Author: JayY
# @Date:   2018-09-28T14:51:58+09:00
# @Filename: new_31.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:36:39+09:00
# @Copyright: JayY

# new_31.py
# practice python
# adding specific words to each sentences
# ======================================================


'''
practice file for making a training file
'''

import numpy as np
import collections

fpr = open('train_skip_01.txt', 'r', encoding='utf-8')
fpw = open('train_skip_01_result.txt', 'w', encoding='utf-8')

window_size = 2
num_skip = window_size*2 + 1

temp_dictionary = dict()
dummy_01, dummy_02, dummy_03, dummy_04 = 0, 1, 2, 3

while True:
    line = fp.readline()
    if not line: break
    line = line.split()
    line_t = line
    line_t.insert(0, dummy_02)
    line_t.insert(0, dummy_01)
    line_t.append(dummy_03)
    line_t.append(dummy_04)
    for i in range(len(line)):
        for j in range(num_skip):
            if j==window_size: continue
            a = temp_dictionary.get(line[i])
            b = temp_dictionary.get(line_t[j])
            a, b = str(a), str(b)
            fpw.write(a + '\t' + b)
