# @Author: JY
# @Date:   2019-02-19T10:11:45+09:00
# @Filename: e_29.py
# @Last modified by:   JY
# @Last modified time: 2019-02-19T11:07:48+09:00
# @Copyright: JeeY

filename_00 = 'train_dataset_raw_01.train'
filename_01 = 'result_raw_words_list_00.words'
filename_03 = 'result_pos_temp_01.pos'

filename_02 = 'train_dataset_raw_02.train'

full_words_dict = dict()
with open(filename_01, 'r', encoding='utf-8') as f:
    num= 0
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        full_words_dict[line[0]] = num
        num += 1

full_pos_list = list()
with open(filename_03, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        full_pos_list.append(line[1])

full_train_list = list()
with open(filename_00, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        line = line.split('#$%')
        if line == ['\n']:
            continue
        one_line = list()
        for i,j in enumerate(line):
            j = j.split()
            if i == 2:
                if j[0] == 'shift':
                    one_line.append(str(0))
                elif j[0] == 'left':
                    one_line.append(str(1))
                elif j[0] == 'right':
                    one_line.append(str(2))
                break
            if j[0] == 'root':
                one_line.append(str(full_words_dict[j[0]]))
                one_line.append(str(full_pos_list.index('root')))
                continue
            for k,l in enumerate(j):
                if k == 0:
                    continue
                if k%2 == 1:
                    one_line.append(str(full_words_dict[str(l)]))
                else:
                    one_line.append(str(full_pos_list.index(l)))
        full_train_list.append(one_line)

with open(filename_02, 'w', encoding='utf-8') as f:
    for i in full_train_list:
        line = '  '.join(i)
        f.write(line + '\n')























## endl
