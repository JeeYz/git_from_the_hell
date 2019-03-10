# @Author: J.Y.
# @Date:   2019-03-09T21:47:13+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-09T22:56:22+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import sys
sys.path.append(r'./module')

import e_38_module_1 as mod1

filename0 = 'result_07.result'
filename1 = 'result_08.result'

full_data = mod1.make_full_initial_raw_dataset(filename0)
print('full data complete...')

modified_data = list()
print(len(full_data))
switch = 1
for i in full_data:
    for j in i[1:]:
        if int(j[1]) > int(i[-1][0]):
            switch = 0
    if switch == 1:
        # print(i)
        modified_data.append(i)
    elif switch == 0:
        switch = 1
print('modifying is complete...')

print(len(modified_data))
# print(modified_data[0])
# print(modified_data[1])
with open(filename1, 'w', encoding='utf-8') as f:
    for i in modified_data:
        # print(i)
        for k,j in enumerate(i):
            # print(j)
            if k == 0:
                line = '  '.join(j)
                f.write(line + '\n')
            else:
                line = '\t'.join(j)
                f.write(line + '\n')
        f.write('\n')

print('generating file is complete...')








## endl
