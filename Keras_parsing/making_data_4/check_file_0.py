# @Author: J.Y.
# @Date:   2019-09-05T12:40:37+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-09-05T12:49:57+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY


trainfile = 'd:/Program_Data/raw_train_dataset_25.train'



with open(trainfile, 'r', encoding='utf-8') as fr:

    while True:
        line = fr.readline()
        if not line:break
        line = line.split()

        print(line)























## endl
