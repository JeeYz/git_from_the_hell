# @Author: J.Y.
# @Date:   2019-04-12T06:03:02+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-12T06:11:34+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

filename2 = 'd:/Program_Data/raw_train_dataset_05.train'
filename3 = 'd:/Program_Data/raw_train_dataset_06.train'

with open(filename3, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        print(line)








## endl
