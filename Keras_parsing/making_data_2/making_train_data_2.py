# @Author: J.Y.
# @Date:   2019-04-12T02:59:49+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-12T10:14:56+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import time
import module_1 as m1

fname0 = 'd:/Program_Data/raw_train_dataset_12.train'
fname1 = 'd:/Program_Data/raw_train_dataset_13.train'

fname2 = 'd:/Program_Data/raw_train_dataset_05.train'

fr2 = open(fname2, 'r', encoding='utf-8')

def make_one_sent_data():
    sent_data = dict()
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
            word = list()
            pos = list()
            one_ele = list()
            word.append(line[3])
            word.append(line[5])
            pos.append(line[4])
            pos.append(line[6])
            one_ele.append(word)
            one_ele.append(pos)
            sent_data[line[2]] = one_ele
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
            words = list()
            poses = list()
            for i in range(18):
                if line[2*i] == 'ROOT':
                    words.append('ROOT')
                    words.append('ROOT')
                    words.append('##')
                    poses.append('ROOT')
                    poses.append('ROOT')
                    poses.append('##')
                elif line[2*i] == 'NULL':
                    words.append('NULL')
                    words.append('NULL')
                    words.append('##')
                    poses.append('NULL')
                    poses.append('NULL')
                    poses.append('##')
                else:
                    words.extend(sent_data[line[2*i]][0])
                    words.append('##')
                    poses.extend(sent_data[line[2*i]][1])
                    poses.append('##')

            new = list()
            new.extend(words)
            new.extend(poses)
            new.append(line[-1])
            if len(new) != 109:
                print(new)
                print(len(new))
                time.sleep(100000)
            fw.write('   '.join(new) + '\n')

fr2.close()



## endl
