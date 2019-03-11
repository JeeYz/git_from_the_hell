# @Author: J.Y.
# @Date:   2019-03-11T09:39:15+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-11T10:30:08+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filepath = 'd:/Program_Data/'
filename0 = 'raw_train_dataset_02.train'

filename1 = 'train_dataset_'
filename2 = '.train'

filename = filepath + filename0

full_data = list()
with open(filename, 'r', encoding='utf-8') as f:
    one_sent = list()
    switch = 0
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        if switch == 1:
            switch = 0
            continue
        if line == []:
            full_data.append(one_sent)
            one_sent = list()
            switch = 1
            continue
        one_sent.append(line)

print(full_data)














## endl
