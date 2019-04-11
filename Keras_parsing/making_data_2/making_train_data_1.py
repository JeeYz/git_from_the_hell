# @Author: J.Y.
# @Date:   2019-04-11T11:06:59+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-11T20:20:52+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import time

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
            switch = 0
            one_sent = list()
            continue
        one = list()
        one.append(line[3])
        one.append(line[5])
        one_sent.append(one)
# print(full_sent_data)
with open(fname0, 'r', encoding='utf-8') as fr, open(fname1, 'a', encoding='utf-8') as fw:
    switch = 1
    for i,j in enumerate(full_sent_data):
        # if i == 2:
        #     print('P A U S E ! !')
        #     time.sleep(10000)
        stack, buffer, action_stack = m0.return_stack_buffer_act_stack(j)
        # print(j)
        num = 0
        while True:
            line = fr.readline()
            if not line: break
            line = line.split()

            # print(' *** %d ***' %num)
            # print('<< stack >>')
            # print(stack, '\n')
            # print('<< buffer >>')
            # print(buffer, '\n')

            if line == []:
                fw.write('\n')
                switch = 1
                num = 0
                break
            if switch == 1:
                new_line, stack, buffer, action_stack = m0.generate_one_train_data(line, switch,
                                                                            stack, buffer, action_stack)
                # print('<< new_line >>')
                # print(new_line, new_line.count('##'), '\n')
                fw.write('   '.join(new_line) + '\n')
                switch = 0
            else:
                new_line, stack, buffer, action_stack = m0.generate_one_train_data(line, switch,
                                                                            stack, buffer, action_stack)
                # print('<< new_line >>')
                # print(new_line, new_line.count('##'), '\n')
                fw.write('   '.join(new_line) + '\n')
            num += 1






## endl
