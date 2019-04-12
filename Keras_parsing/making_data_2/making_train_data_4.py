# @Author: J.Y.
# @Date:   2019-04-12T10:38:17+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-12T11:09:35+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import module_1 as m1
sents_num = 2500

fname0 = 'd:/Program_Data/raw_train_dataset_14.train'

with open(fname0, 'r', encoding='utf-8') as fr:
    switch = 0
    num = 0
    filenum = 0
    sents = list()
    while True:
        if switch == 1:
            print('%d sentences complete!!' %num)
            filenum += 1
            switch = 0
        line = fr.readline()
        if not line:break
        line = line.split()
        if line == []:
            num += 1
            m1.write_new_divided_train_data(filenum, sents)
            sents = list()
            if num != 0 and num%sents_num == 0:
                switch = 1
        sents.append(line)









## endl
