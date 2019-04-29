# @Author: J.Y.
# @Date:   2019-04-29T04:11:11+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-29T10:19:51+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

fname0 = 'd:/Program_Data/raw_train_dataset_05.train'
fname1 = 'd:/Program_Data/raw_train_dataset_20.train'

train_data = list()

with open(fname0, 'r', encoding='utf-8') as f:
    switch = 1
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        if line == []:
            switch = 1
            train_data.append(new)
            continue
        if switch == 1:
            switch = 0
            new = list()
            continue
        new.append(line[2:])

with open(fname1, 'w', encoding='utf-8') as fw:
    for sent in train_data:
        for word in sent:
            fw.write('    '.join(word) + '\n')
        fw.write('\n')







## endl
