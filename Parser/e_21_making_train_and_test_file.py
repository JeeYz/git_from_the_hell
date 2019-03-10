# @Author: JY
# @Date:   2019-02-13T09:46:12+09:00
# @Filename: e_21.py
# @Last modified by:   JY
# @Last modified time: 2019-02-13T10:44:49+09:00
# @Copyright: JeeY

import random as rand
import time as ti

filename00 = 'result_05.result'

filename01 = 'train_dataset_raw_00.train'
filename02 = 'test_dataset_raw_00.test'

# full_result_list = list()
# temp_stack =list()
# temp_buffer = list()

train_list = list()
test_list = list()

# print(rand.random())

with open(filename00, 'r', encoding='utf-8') as fr:
    ppara = 0
    switch = 1
    evacu = 1
    while evacu:
        temp = list()
        if len(test_list) == 10000:
            switch = 0
        if switch == 1:
            prob = rand.random()
        else:
            prob = 0.5
        while True:
            if 0.8 < prob:
                line = fr.readline()
                if not line:
                    evacu = 0
                    break
                line = line.split()
                if line == []:
                    test_list.append(temp)
                    break
                temp.append(line)
            else:
                line = fr.readline()
                if not line:
                    evacu = 0
                    break
                line = line.split()
                if line == []:
                    train_list.append(temp)
                    break
                temp.append(line)

print(len(train_list))
print(len(test_list))

with open(filename01, 'w', encoding='utf-8') as f1, open(filename02, 'w', encoding='utf-8') as f2:
    for x in train_list:
        for y,z in enumerate(x):
            if y == 0:
                temp = ' '.join(z)
                f1.write(temp + '\n')
            else:
                temp = '\t'.join(z)
                f1.write(temp + '\n')
        f1.write('\n')

    for x in test_list:
        for y,z in enumerate(x):
            if y == 0:
                temp = ' '.join(z)
                f2.write(temp + '\n')
            else:
                temp = '\t'.join(z)
                f2.write(temp + '\n')
        f2.write('\n')









## endl
