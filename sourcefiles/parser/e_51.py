# @Author: J.Y.
# @Date:   2019-03-04T11:56:05+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-04T14:18:49+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import sys
# print(sys.path)
sys.path.append(r'.\module')
# print(sys.path)
import e_36_module_0 as mod0
import e_38_module_1 as mod1

filename3 = 'result_05.result'

full_data = mod1.make_full_initial_raw_dataset(filename3)
print('full_data complete...')

filename0 = 'result_modified_pos_data_05.pos'
filename1 = 'temp_result_08.temp'
filename2 = 'temp_result_08_v01.temp'

pos_dict = dict()
with open(filename0, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        pos_dict[line[1]] = line[5]
print('pos_dict complete...')

modified_pos_data = list()
with open(filename1, 'r', encoding='utf-8') as f:
    one_sent = list()
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if line == []:
            one_sent[-1][-1] = '문미기호'
            modified_pos_data.append(one_sent)
            one_sent = list()
        else:
            one_line = list()
            for i in line:
                one_line.append(pos_dict[i])
            one_sent.append(one_line)
print('modified_pos_data complete...')

print(len(modified_pos_data))
print(len(full_data))

with open(filename2, 'w', encoding='utf-8') as f:
    for i in modified_pos_data:
        for j in i:
            line = '\t\t'.join(j)
            f.write(line + '\n')
        f.write('\n')




## endl
