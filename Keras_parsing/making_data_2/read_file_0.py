# @Author: J.Y.
# @Date:   2019-04-12T06:03:02+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-18T10:42:54+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import time

filename0 = 'd:/Program_Data/result_06.result'
filename1 = 'd:/Program_Data/raw_train_dataset_00.train'
filename2 = 'd:/Program_Data/raw_train_dataset_05.train'
filename3 = 'd:/Program_Data/raw_train_dataset_06.train'
filename4 = 'd:/Program_Data/raw_train_dataset_11.train'
filename5 = 'd:/Program_Data/raw_train_dataset_13.train'
filename6 = 'd:/Program_Data/raw_train_dataset_14.train'

with open(filename1, 'r', encoding='utf-8') as f:
    num = 0
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        if line == []:
            num += 1
            continue
        # if line.count('##') != 6:
        #     print(line)
        # if len(line) != 109:
        #     print(line)
        # num += 1
        # print(line)
        # print(len(line))
        # if num == 5:
        #     time.sleep(10000)

print(num)





## endl
