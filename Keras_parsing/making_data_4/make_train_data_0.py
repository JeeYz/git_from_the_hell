# @Author: J.Y.
# @Date:   2019-09-05T10:31:03+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-09-05T12:59:47+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY


import time

trainfile = 'd:/Program_Data/raw_train_dataset_24.train'
trainfile2 = 'd:/Program_Data/raw_train_dataset_25.train'

with open(trainfile, 'r', encoding='utf-8') as fr:
    num = 0
    max = 0
    while True:
        line = fr.readline()
        if not line:break
        line = line.split()

        if line == []:

            if max == 0:
                max = num
            else:
                if num > max:
                    max = num
            num = 0


        num += 1

print(max)


with open(trainfile, 'r', encoding='utf-8') as fr, open(trainfile2, 'w', encoding='utf-8') as fw:
    num = 0
    while True:
        line = fr.readline()
        if not line:break
        line = line.split()

        if line == []:
            new = ['0', '0', 'NULL', '0', '0', '0', '0']
            for i in range(max-num):
                new2 = '    '.join(new)
                # print(new2)
                fw.write(new2)
                fw.write('\n')
            # fw.write('\n')
            num = 0

        new = list()
        new = '    '.join(line)
        fw.write(new)
        fw.write('\n')
        num += 1


with open(trainfile2, 'r', encoding='utf-8') as fr:
    num = 0
    while True:
        line = fr.readline()
        if not line:break
        line = line.split()

        if line == []:
            if num != max:
                print(num)
            num = 0

        num += 1














## endl
