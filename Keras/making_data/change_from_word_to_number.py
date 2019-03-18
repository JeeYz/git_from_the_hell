# @Author: J.Y.
# @Date:   2019-03-15T07:25:12+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-18T11:52:50+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import sys
sys.path.append(r'C:/Users/AI_LAB/Desktop/Github/git_from_the_hell/Parser/module')
import e_57_module_3 as m3

words_dict, pos_dict = m3.return_data_of_words(2)

filename0 = 'd:/Program_Data/raw_train_dataset_07.train'
filename1 = 'd:/Program_Data/raw_train_dataset_08.train'

with open(filename0, 'r', encoding='utf-8') as f1,\
open(filename1, 'a', encoding='utf-8') as f2:
    while True:
        line = f1.readline()
        if not line:break
        line = line.split()
        if line == []:
            f2.write('\n')
            continue
        num1 = 1
        new_line = list()
        for i in line:
            if i == '##':
                num1 += 1
                new_line.append('##')
            else:
                if num1 > 18:
                    if i == 'shift':
                        new_line.append(str(0))
                    elif i == 'left':
                        new_line.append(str(1))
                    elif i == 'right':
                        new_line.append(str(2))
                    else:
                        new_line.append(str(pos_dict[i]))
                else:
                    new_line.append(str(words_dict[i]))
        a = '\t'.join(new_line)
        f2.write(a + '\n')









## endl
