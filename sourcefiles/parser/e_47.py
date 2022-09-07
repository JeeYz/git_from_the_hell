# @Author: J.Y.
# @Date:   2019-03-04T01:29:12+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-04T10:16:41+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import sys
# print(sys.path)
sys.path.append(r'.\module')
# print(sys.path)
import e_36_module_0 as mod0
import e_38_module_1 as mod1

filename0 = 'result_05.result'
filename1 = 'result_00_pos_sentence.sentence'

full_data = mod1.make_full_initial_raw_dataset(filename0)

print(full_data[0])

full_sent_data = list()
for i in full_data:
    one_line = list()
    for j in i[1:]:
        for k,l in enumerate(j[3:]):
            if k%2==1:
                one_line.append(l)
    full_sent_data.append(one_line)

print(full_sent_data[0])

with open(filename1, 'w', encoding='utf-8') as f:
    for i in full_sent_data:
        line = ' '.join(i)
        f.write(line + '\n\n')








## endl
