# @Author: J.Y.
# @Date:   2019-03-19T20:34:47+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-19T20:44:18+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

filename1 = 'd:/Program_Data/raw_train_dataset_08.train'
filename2 = 'd:/Program_Data/raw_train_dataset_07.train'
filename3 = 'd:/Program_Data/raw_train_dataset_06.train'

with open(filename3, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        if line == []: continue
        # if len(line) != 109:
        #     print(line)
        print(len(line))




## endl
