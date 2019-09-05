# @Author: J.Y.
# @Date:   2019-09-05T13:36:43+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-09-05T17:43:58+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY


fpath = 'd:/Program_Data/Parsing_Data_BiLSTM_batch/'

def write_new_divided_train_data(filenum, sents):
    fname = fpath + 'parsing_BiLSTM_batch_train_data_%02d.train' %filenum
    with open(fname, 'a', encoding='utf-8') as fw:
        for line in sents:
            fw.write('  '.join(line) + '\n')
        fw.write('\n')

trainfile1 = 'd:/Program_Data/raw_train_dataset_25.train'

sents_num = 5000

with open(trainfile1, 'r', encoding='utf-8') as fr:
    switch = 0
    num = 0
    filenum = 0
    sents = list()
    while True:
        if switch == 1:
            print('%d sentences complete!!' %num)
            filenum += 1
            switch = 0
            continue
        line = fr.readline()
        if not line:break
        line = line.split()
        if line == []:
            num += 1
            write_new_divided_train_data(filenum, sents)
            sents = list()
            if num != 0 and num%sents_num == 0:
                switch = 1
            continue
        sents.append(line)























## endl
