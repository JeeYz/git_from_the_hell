# @Author: J.Y.
# @Date:   2019-03-04T05:33:46+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-04T10:50:46+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import sys
# print(sys.path)
sys.path.append(r'.\module')
# print(sys.path)
import e_36_module_0 as mod0
import e_38_module_1 as mod1

filename0 = 'result_modified_pos_data_05.pos'

pos_dict = dict()
with open(filename0, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        pos_dict[line[1]] = line[5]
print('pos_dict complite!!')

filename1 = 'result_05.result'
full_data = mod1.make_full_initial_raw_dataset(filename1)
print('full_data complete!!')

filename2 = 'temp_result_03.temp'
filename3 = 'temp_result_03_v01.temp'

before_data_list = list()
with open(filename2, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        before_data_list.append(line)
print('before_data_list complete!!')

after_data_list = list()
for i in before_data_list:
    line = list()
    for j in i:
        if j == '문미기호':
            line.append('문미기호')
        else:
            line.append(pos_dict[j])
    after_data_list.append(line)
print('after_data_list complete!!')

with open(filename3, 'w', encoding='utf-8') as f:
    for i in after_data_list:
        line = '\t\t'.join(i)
        f.write(line + '\n')
        if i[-1] == '문미기호':
            f.write('\n')
print('making file complete!!')




## endl
