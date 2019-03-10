# @Author: J.Y.
# @Date:   2019-02-27T11:01:54+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-02-27T15:40:04+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filename0 = 'temp_result_01.temp'
filename1 = 'temp_result_02.temp'
filename2 = 'temp_result_03.temp'
filename3 = 'temp_result_07.temp'

with open(filename0, 'r', encoding='utf-8') as f, \
open(filename1, 'r', encoding='utf-8') as f2, \
open(filename2, 'r', encoding='utf-8') as f3:
    pos_list = list()
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        pos_list.append(line)
    while True:
        line = f2.readline()
        if not line: break
        line = line.split()
        pos_list.append(line)

    data_pos = list()
    while True:
        line = f3.readline()
        if not line: break
        line = line.split()
        data_pos.append(line)

temp = list()
for i in data_pos:
    if i not in temp:
        temp.append(i)

for i in temp:
    if i not in pos_list:
        print(i)

temp.sort()

with open(filename3, 'w', encoding='utf-8') as f:
    for i in temp:
        line = '\t'.join(i)
        f.write(line + '\n')
























## endl
