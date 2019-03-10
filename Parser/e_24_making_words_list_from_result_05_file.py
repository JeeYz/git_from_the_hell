# @Author: JeeY
# @Date:   2019-02-14T05:24:01+09:00
# @Last modified by:   JY
# @Last modified time: 2019-02-14T11:50:31+09:00
# @License: JY
# @Copyright: JY

import time as ti
import copy

filename00 = 'result_05.result'
filename01 = 'result_raw_words_list_00.words'


full_word_dict = dict()

with open(filename00, 'r', encoding='utf-8') as f:
    switch = 1
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if switch == 1:
            switch = 0
            continue
        if line == []:
            switch = 1
            continue
        for i,j in enumerate(line[3:]):
            if i%2 == 0:
                if j in full_word_dict:
                    full_word_dict[j] += 1
                else:
                    word = copy.deepcopy(j)
            else:
                full_word_dict[word] = int(1)

t_dict = sorted(full_word_dict.items())
del full_word_dict
full_word_dict = dict()
for i in t_dict:
    full_word_dict[i[0]] = int(i[1])

# for i in full_word_dict:
#     print(i, '\t', full_word_dict[i])

with open(filename01, 'w', encoding='utf-8') as f:
    for i in full_word_dict:
        f.write(str(i) + '\t\t' + str(full_word_dict[i]) + '\n')




















## endl
