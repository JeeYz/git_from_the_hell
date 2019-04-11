# @Author: J.Y.
# @Date:   2019-04-12T02:59:49+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-12T06:01:26+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import time
import module_1 as m1

fname0 = 'd:/Program_Data/raw_train_dataset_08.train'
fname1 = 'd:/Program_Data/raw_train_dataset_09.train'

fname2 = 'd:/Program_Data/raw_train_dataset_05.train'

fr2 = open(fname2, 'r', encoding='utf-8')

def make_one_sent_data():
    sent_data = list()
    switch = 1
    while True:
        line = fr2.readline()
        if not line:break
        line = line.split()
        if line == []:
            break
        if switch == 1:
            switch = 0
        else:
            ele = list()
            a_word = list()
            ele.append(line[3])
            ele.append(line[5])
            a_word.append(ele)
            a_word.append(line[2])
            sent_data.append(a_word)
    return sent_data

with open(fname0, 'r', encoding='utf-8') as fr, open(fname1, 'a', encoding='utf-8') as fw:
    sent_data = make_one_sent_data()
    while True:
        line = fr.readline()
        if not line:break
        line = line.split()
        if line == []:
            sent_data = make_one_sent_data()
            fw.write('\n')
        else:
            new = list()
            for i in range(18):
                if line[3*i] == 'ROOT':
                    new.append('ROOT')
                    new.append('##')
                elif line[3*i] == 'NULL':
                    new.append('NULL')
                    new.append('##')
                else:
                    for j in sent_data:
                        if line[3*i] == j[0][0] and line[3*i+1] == j[0][1]:
                            new.append(j[1])
                    new.append('##')
            new.append(line[-1])
            if len(new) != 37:
                print(new)
                print(len(new))
                time.sleep(100000)
            fw.write('   '.join(new) + '\n')

fr2.close()



## endl
