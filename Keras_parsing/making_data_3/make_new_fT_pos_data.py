# @Author: J.Y.
# @Date:   2019-04-18T10:44:10+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-18T10:56:53+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filename0 = 'd:/Program_Data/result_06.result'
f_new = 'D:/Program_Data/fastText/fastText-0.1.0/result/train_fT_pos_00'

with open(filename0, 'r', encoding='utf-8') as fr, open(f_new, 'a', encoding='utf-8') as fw:
    switch = 0
    new = list()
    while True:
        line = fr.readline()
        if not line: break
        line = line.split()
        if switch == 0:
            switch = 1
            new = list()
            continue
        if line == []:
            switch = 0
            new.insert(0, 'ROOT')
            fw.write('   '.join(new) +'\n')
            continue

        for i,j in enumerate(line[3:]):
            if i%2 == 1:
                new.append(j)
















## endl
