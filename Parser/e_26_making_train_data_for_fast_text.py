# @Author: JY
# @Date:   2019-02-18T09:54:51+09:00
# @Filename: e_26.py
# @Last modified by:   JY
# @Last modified time: 2019-02-18T15:55:14+09:00
# @Copyright: JeeY

filename_00 = 'result_05.result'
filename_01 = 'train_dataset_for_fastText_00.fastText'

full_list = list()

with open(filename_00, 'r', encoding='utf-8') as f:
    switch = 1
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if switch == 1:
            one_sent = list()
            switch = 0
            continue
        if line == []:
            full_list.append(one_sent)
            switch = 1
            continue

        for i,j in enumerate(line[3:]):
            if i%2 == 0:
                one_sent.append(j)

with open(filename_01, 'w', encoding='utf-8') as f:
    for i in full_list:
        line = ' '.join(i)
        f.write(line + '\n')












## endl
