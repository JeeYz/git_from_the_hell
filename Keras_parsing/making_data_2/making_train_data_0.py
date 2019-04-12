# @Author: J.Y.
# @Date:   2019-04-11T10:28:00+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-12T09:45:40+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

fname0 = 'd:/Program_Data/raw_train_dataset_10.train'
fname1 = 'd:/Program_Data/raw_train_dataset_11.train'

with open(fname0, 'r', encoding='utf-8') as f, open(fname1, 'a', encoding='utf=8') as fw:
    while True:
        new = list()
        line = f.readline()
        if not line:break
        line = line.split()
        if line == []:
            fw.write('\n')
            continue
        for i in range(6):
            new.append(line[i*2])
            new.append('##')
        new.append(line[-1])
        new = '    '.join(new)
        fw.write(new + '\n')













## endl
