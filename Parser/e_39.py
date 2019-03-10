# @Author: J.Y.
# @Date:   2019-02-26T04:33:54+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-02-27T10:08:43+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import sys
sys.path.append('./module/')
import e_38_module_1 as  mod1

filename_00 = 'result_05.result'
filename_01 = 'result_pos_temp_01.pos'

filename_02 = 'temp_result_00.temp'
filename_03 = 'temp_result_01.temp'
filename_04 = 'temp_result_02.temp'

full_initial_data = mod1.make_full_initial_raw_dataset(filename_00)

list_00 = list()
for i in full_initial_data:
    for m in i[1:]:
        one_line = list()
        for l,n in enumerate(m[3:]):
            if l%2 == 1:
                one_line.append(n)
        list_00.append(one_line)

with open(filename_01, 'r', encoding='utf-8') as f:
    list_01 = []
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        list_01.append(line[1])

list_02 = list()
for i in list_01:
    for j in list_01:
        one_line = list()
        one_line.append(i)
        one_line.append(j)
        list_02.append(one_line)

del list_01
list_03 = list()
for i in list_00:
    if len(i)==1:
        list_03.append(i)

list_04 =list()
for i in list_03:
    if i in list_04:
        continue
    else:
        list_04.append(i)
del list_03

# list_00 -> pos pairs of raw data
# list_02 -> pos pair's list from pos data
# list_04 -> single pos

with open(filename_02, 'w', encoding='utf-8') as f1, \
open(filename_03, 'w', encoding='utf-8') as f2, \
open(filename_04, 'w', encoding='utf-8') as f3:
    for i in list_00:
        line = '\t'.join(i)
        f1.write(line + '\n')
    for i in list_02:
        line = '\t'.join(i)
        f2.write(line + '\n')
    for i in list_04:
        line = '\t'.join(i)
        f3.write(line + '\n')













## endl
