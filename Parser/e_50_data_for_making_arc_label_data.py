# @Author: J.Y.
# @Date:   2019-03-04T11:19:03+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-04T14:18:29+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import sys
# print(sys.path)
sys.path.append(r'.\module')
# print(sys.path)
import e_36_module_0 as mod0
import e_38_module_1 as mod1

filename0 = 'result_05.result'
filename1 = 'temp_result_08.temp'

full_data = mod1.make_full_initial_raw_dataset(filename0)
print('making full_data list complete...')

pos_data = list()
for i in full_data:
    one_sent = list()
    for j in i[1:]:
        line = list()
        for k,l in enumerate(j[3:]):
            if k%2 == 1:
                line.append(l)
        one_sent.append(line)
    pos_data.append(one_sent)
print('making pos_data complete...')

if len(full_data) == len(pos_data):
    print('number of pos_data is correct...')
else:
    print('number of pos_data is incorrect...')

print(full_data[0])
print(pos_data[0])

modified_pos_data = list()
for i in pos_data:
    one_sent = list()
    for j in i:
        line = list()
        if '긍정지정사' in j:
            line.append('긍정지정사')
        else:
            if len(j) > 1:
                line.append(j[0])
                line.append(j[-1])
            else:
                line.append(j[0])
        one_sent.append(line)
    modified_pos_data.append(one_sent)

print('making modified_pos_data complete...')
print(len(full_data))
print(len(modified_pos_data))

for i in modified_pos_data:
    for j in i:
        if len(j) > 2:
            print(i)

print('checking complete...')

with open(filename1, 'w', encoding='utf-8') as f:
    for i in modified_pos_data:
        for j in i:
            line = '\t\t'.join(j)
            f.write(line + '\n')
        f.write('\n')











## endl
