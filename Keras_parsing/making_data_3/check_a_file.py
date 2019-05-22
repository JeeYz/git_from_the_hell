# @Author: J.Y.
# @Date:   2019-05-22T14:26:02+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-22T14:33:14+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import time

trainfile3 = 'd:/Program_Data/raw_train_dataset_24.train'

with open(trainfile3, 'r', encoding='utf-8') as f:
    one_s = list()
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if line == []:
            if int(one_s[-1]) != 0:
                print(one_s)
                time.sleep(100000)
            one_s = list()
            continue
        one_s.append(line[2])
        one_s.append(line[1])










## endl
