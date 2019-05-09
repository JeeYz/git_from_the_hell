# @Author: J.Y.
# @Date:   2019-05-09T11:29:24+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-09T13:26:56+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

trainfile = 'd:/Program_Data/raw_train_dataset_23.train'

def make_small_train_data():
    word = list()
    pos = list()
    label = list()
    sent_w = list()
    sent_p = list()
    with open(trainfile, 'r', encoding='utf-8') as f:
        switch = 1
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                switch = 2
                continue
            if switch == 2:
                label.append([line[0], line[1]])
                continue
            word.append([line[1], line[2]])
            pos.append([line[3], line[4]])
    print(word)
    print(pos)
    print(label)
    return [word], [pos], label



## endl
