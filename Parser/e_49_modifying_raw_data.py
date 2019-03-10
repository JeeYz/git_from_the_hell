# @Author: J.Y.
# @Date:   2019-03-04T10:18:11+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-04T11:18:50+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import sys
# print(sys.path)
sys.path.append(r'.\module')
# print(sys.path)
import e_36_module_0 as mod0
import e_38_module_1 as mod1

filename0 = 'result_05.result'
filename1 = 'temp_result_03_v01.temp'
filename2 = 'result_06.result'

full_data = mod1.make_full_initial_raw_dataset(filename0)

pos_data = list()
with open(filename1, 'r', encoding='utf-8') as f:
    one_sent = list()
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if line == []:
            pos_data.append(one_sent)
            one_sent = list()
            continue
        one_sent.append(line)

print(len(full_data))
print(len(pos_data))

for i,j in enumerate(full_data):
    for m,n in enumerate(i[1:]):
        line = '_'.join(pos_data[i][m])
        n.append(line)
print('making file begin...')
with open(filename2, 'w', encoding='utf-8') as f:
    for i in full_data:
        for j,k in enumerate(i):
            if j == 0:
                line = '  '.join(k)
                f.write(line + '\n')
            else:
                line = '\t\t'.join(k)
                f.write(line + '\n')
        f.write('\n')

print('complete...!!!')






## endl
