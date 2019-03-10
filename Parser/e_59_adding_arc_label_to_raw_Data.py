# @Author: J.Y.
# @Date:   2019-03-09T04:30:24+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-09T04:52:41+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import sys
sys.path.append(r'./module')

import e_38_module_1 as mod1
import e_56_module_2 as mod2

filename0 = 'result_06.result'
filename1 = 'result_07.result'

filename2 = 'temp_result_08_v02.temp'

full_data = mod1.make_full_initial_raw_dataset(filename0)
print('full data complete...')
arc_data = mod2.making_arc_list(filename2)
print('arc data complete...')

print(len(full_data))
print(len(arc_data))

for i,j in enumerate(full_data):
    for k,l in enumerate(j):
        if k == 0:
            continue
        l.append(arc_data[i][k-1])

print('modifying complete...')
with open(filename1, 'w', encoding='utf-8') as f:
    for i in full_data:
        for m,n in enumerate(i):
            if m == 0:
                line = '  '.join(n)
                f.write(line + '\n')
            else:
                line = '\t'.join(n)
                f.write(line + '\n')
        f.write('\n')






## endl
