# @Author: J.Y.
# @Date:   2019-03-26T11:36:01+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-27T14:13:05+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

fpath1 = 'd:/Program_Data/'
filename1 = fpath1 + 'raw_test_dataset_04.test'
filename2 = fpath1 + 'raw_test_dataset_05.test'
filename3 = fpath1 + 'raw_test_dataset_01.test'

with open(filename1, 'r', encoding='utf-8') as f1, open(filename2, 'a', encoding='utf-8') as f2:
    switch = 1
    while True:
        line = f1.readline()
        if not line:break
        line = line.split()
        if switch == 1:
            for i in range(2):
                line = f1.readline()
            line = f1.readline()
            if not line:break
            line = line.split()
            new = list()
            for i,j in enumerate(line[:-2], 1):
                if j == '##':
                    new.append('##')
                elif i < 18:
                    new.append(j)
                elif 54 < i and i < 72:
                    new.append(j)
                else:
                    new.append(str(0))

            f2.write('\t'.join(new) + '\n\n')
            switch = 0
            continue
        if line == []:
            switch = 1
            continue
















## endl
