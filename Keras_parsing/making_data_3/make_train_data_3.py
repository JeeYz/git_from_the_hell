# @Author: J.Y.
# @Date:   2019-05-09T11:30:05+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-20T16:19:09+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

trainfile = 'd:/Program_Data/raw_train_dataset_22.train'
trainfile1 = 'd:/Program_Data/raw_train_dataset_05.train'
trainfile2 = 'd:/Program_Data/raw_train_dataset_23.train'

with open(trainfile, 'r', encoding='utf-8') as fr, open(trainfile2, 'a', encoding='utf-8') as fw:
    while True:
        line = fr.readline()
        if not line:break
        line = line.split()
        if line == []:
            fw.write('\n')
            break
        fw.write('    '.join(line) + '\n')

with open(trainfile1, 'r', encoding='utf-8') as fr, open(trainfile2, 'a', encoding='utf-8') as fw:
    switch = 1
    while True:
        line = fr.readline()
        if not line:break
        line = line.split()
        if line == []:
            fw.write('\n')
            break
        if switch == 1:
            switch = 0
            continue
        new = line[:2]
        fw.write('    '.join(new) + '\n')



## endl
