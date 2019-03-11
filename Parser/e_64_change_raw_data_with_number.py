# @Author: J.Y.
# @Date:   2019-03-10T16:47:15+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-11T09:38:18+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import time
import copy
import sys

sys.path.append(r'.\module')

import e_36_module_0 as mod0
import e_38_module_1 as mod1
import e_56_module_2 as mod2
import e_57_module_3 as mod3

filename0 = 'raw_train_dataset_01.train'
filename1 = 'raw_train_dataset_02.train'

filename4 = 'result_raw_words_list_00.words'
filename5 = 'result_modified_pos_data_05.pos'
filename6 = 'temp_result_09.temp'

word_dict = mod3.making_dictionary_of_words(filename4)
pos_dict = mod3.making_pos_dictionary(filename5)
arc_dict = mod3.making_arc_dictionary(filename6)

with open(filename0, 'r', encoding='utf-8') as f1,\
open(filename1, 'w', encoding='utf-8') as f2:
    while True:
        line = f1.readline()
        if not line:break
        line = line.split()
        if line == []:
            f2.write('\n\n')
            # time.sleep(100000)
            continue
        para_num = 0
        switch = 0
        m_line = list()
        for i in line[:-1]:
            if i == '##':
                para_num += 1
                m_line.append('##')
                if para_num == 18 or para_num == 36:
                    switch += 1
            else:
                if switch == 0:
                    m_line.append(str(word_dict[i]))
                elif switch == 1:
                    m_line.append(str(pos_dict[i]))
                else:
                    m_line.append(str(arc_dict[i]))

        if line[-1] == 'shift':
            m_line.append(str(0))
        elif line[-1] == 'left':
            m_line.append(str(1))
        elif line[-1] == 'right':
            m_line.append(str(2))

        # print(m_line)
        m1_line = '\t'.join(m_line)
        f2.write(m1_line + '\n')








## endl
