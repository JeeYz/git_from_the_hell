# @Author: J.Y.
# @Date:   2019-03-11T09:39:15+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-12T11:33:32+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filepath = 'd:/Program_Data/'
filename0 = 'raw_train_dataset_02.train'

filename = filepath + filename0

full_data = list()
with open(filename, 'r', encoding='utf-8') as f:
    one_sent = list()
    switch = 0
    sent_num = 0
    file_num = 0
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        if switch == 1:
            switch = 0
            sent_num += 1
            if sent_num%5000 == 0:
                file_1 = filepath + 'result_train_dataset_%02d.train' %file_num
                with open(file_1, 'w', encoding='utf-8') as fw:
                    for i in full_data:
                        for j in i:
                            line1 = '\t'.join(j)
                            fw.write(line1 + '\n')
                        fw.write('\n')
                    del full_data
                    full_data = list()
                    file_num += 1
                    print('generating file complete...\n')
            continue
        if line == []:
            full_data.append(one_sent)
            one_sent = list()
            switch = 1
            continue
        one_sent.append(line)

file_1 = filepath + 'result_train_dataset_%02d.train' %file_num
with open(file_1, 'w', encoding='utf-8') as fw:
    for i in full_data:
        for j in i:
            line1 = '\t'.join(j)
            fw.write(line1 + '\n')
        fw.write('\n')
    del full_data
    full_data = list()
    file_num += 1
    print('generating file complete...\n')

print('\n ** All files are complete... **')














## endl
