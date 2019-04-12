# @Author: J.Y.
# @Date:   2019-04-12T10:18:55+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-12T10:37:47+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import time
import sys
# sys.path.append(r'C:/Users/AI_LAB/Desktop/Github/git_from_the_hell/Keras_parsing/module')
sys.path.append(r'../module')

import parsing_module_0 as p0

fname0 = 'd:/Program_Data/raw_train_dataset_13.train'
fname1 = 'd:/Program_Data/raw_train_dataset_14.train'

words_dict, pos_dict = p0.make_words_pos_dict()
print(pos_dict)
with open(fname0, 'r', encoding='utf-8') as fr, open(fname1, 'a', encoding='utf-8') as fw:
    num = 0
    while True:
        line = fr.readline()
        if not line:break
        line = line.split()
        if line == []:
            fw.write('\n')
        else:
            # print(line)
            new_line = list()
            for i in line[:54]:
                if i == '##':
                    new_line.append('##')
                else:
                    new_line.append(str(words_dict[i]))
            for j in line[54:-1]:
                if j == '##':
                    new_line.append('##')
                else:
                    new_line.append(str(pos_dict[j]))
            new_line.append(line[-1])

            if len(new_line) != 109:
                print(new_line)
                print(len(new_line))
                time.sleep(100000)
            fw.write('   '.join(new_line) + '\n')
        # num += 1
        # if num == 5:
        #     time.sleep(100000)






## endl
