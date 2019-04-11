# @Author: J.Y.
# @Date:   2019-04-11T11:06:59+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-11T15:00:15+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

fname0 = 'd:/Program_Data/raw_train_dataset_07.train'
fname1 = 'd:/Program_Data/raw_train_dataset_08.train'

fname2 = 'd:/Program_Data/raw_train_dataset_05.train'

import module_0 as m0

full_sent_data = list()
with open(fname2, 'r', encoding='utf-8') as f:
    switch = 1
    one_sent = list()
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if line == []:
            switch = 1
            full_sent_data.append(one_sent)
            continue
        if switch == 1:
            switch == 0
            one_sent = list()
            continue
        one = list()
        one.append(line[3])
        one.append(line[5])

with open(fname0, 'r', encoding='utf-8') as fr, open(fname1, 'a', encoding='utf-8') as fw,\
open(fname2, 'r', encoding='utf-8') as fr2:
    switch = 1
    for i,j in enumerate(full_sent_data):
        action_stack = list()
        stack, buffer = m0.return_stack_buffer(j)
        while True:
            line = fr1.readline()
            if not line: break
            line = line.split()
            if line == []:
                fw.write('\n')
                switch = 1
                break
            if switch == 1:
                new_line, action_stack = m0.generate_one_train_data(line, switch, action_stack)
                switch == 0
                continue
            new_line, action_stack = m0.generate_one_train_data(line, switch, action_stack)







## endl
