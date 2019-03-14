# @Author: J.Y.
# @Date:   2019-03-14T14:50:18+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-14T14:54:46+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

fpath = 'd:/Program_Data/'
filename1 = 'raw_train_dataset_03.train'

with open(fpath + filename1, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        if line == []: continue
        if line.count('##') != 36:
            print(line)














## endl
