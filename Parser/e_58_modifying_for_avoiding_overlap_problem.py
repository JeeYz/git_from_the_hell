# @Author: J.Y.
# @Date:   2019-03-09T03:03:36+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-09T04:38:34+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import sys
sys.path.append(r'./module')

import copy
import time

import e_38_module_1 as mod1

filename0 = 'train_dataset_raw_00.train'
filename1 = 'train_dataset_raw_03.train'
filename2 = 'result_05.result'
filename3 = 'test_dataset_raw_00.test'
filename4 = 'result_06.result'

full_data = mod1.make_full_initial_raw_dataset(filename2)

full_data_modified = copy.deepcopy(full_data)
del full_data
for i,j in enumerate(full_data_modified):
    for k,l in enumerate(j):
        if k == 0:
            for m,n in enumerate(l):
                l[m] = str(n) + '__' + str(m+1)
            # print(l)
        else:
            l[2] = str(l[2]) + '__' + str(k)

print('full modified data is complete...')
with open(filename4, 'w', encoding='utf-8') as f:
    for i in full_data_modified:
        for m,n in enumerate(i):
            if m == 0:
                line = '  '.join(n)
                f.write(line + '\n')
            else:
                line = '\t'.join(n)
                f.write(line + '\n')
        f.write('\n')











## endl
