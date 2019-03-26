# @Author: J.Y.
# @Date:   2019-03-26T11:36:01+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-26T11:52:06+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

fpath1 = 'd:/Program_Data/'
filename1 = fpath1 + 'raw_test_dataset_04.test'
filename2 = fpath1 + 'raw_test_dataset_05.test'

with open(filename1, 'r', encoding='utf-8') as f1, open(filename2, 'a', encoding='utf-8') as f2:
    switch = 1
    while True:
        line = f1.readline()
        if not line:break
        line = line.split()
        if switch == 1:
            f2.write('\t'.join(line) + '\n\n')
            switch = 0
            continue
        if line == []:
            switch = 1
            continue
















## endl
