# @Author: J.Y.
# @Date:   2019-03-14T15:25:44+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-14T15:30:45+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

fpath = 'd:/Program_Data/'
filename0 = 'raw_train_dataset_00.train'
filename1 = 'raw_train_dataset_04.train'

with open(fpath + filename0, 'r', encoding='utf-8') as f1,\
open(fpath + filename1, 'a', encoding='utf-8') as f2:
    switch = 0
    while True:
        line = f1.readline()
        if not line:break
        line = line.split()
        if line == []:
            switch = 0
            f2.write('\n')
            continue
        if switch == 0:
            a = '  '.join(line)
            f2.write(a + '\n')
            switch = 1
        elif switch == 1:
            a = '\t\t'.join(line[:-1])
            f2.write(a + '\n')



## endl
