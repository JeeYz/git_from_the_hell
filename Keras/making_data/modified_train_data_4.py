# @Author: J.Y.
# @Date:   2019-03-14T15:32:13+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-15T06:30:17+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

fpath = 'd:/Program_Data/'
filename0 = 'raw_test_dataset_00.test'
filename1 = 'raw_test_dataset_01.test'

with open(fpath + filename0, 'r', encoding='utf-8') as f1,\
open(fpath + filename1, 'a', encoding='utf-8') as f2:
    switch = 0
    while True:
        line = f1.readline()
        if not line:break
        line = line.split()
        if line == []:
            switch = 0
            f2.write('\n')
            continue
        if switch == 0:
            a = '  '.join(line)
            f2.write(a + '\n')
            switch = 1
        elif switch == 1:
            new_line = list()
            new_line.append(line[0])
            new_line.append(line[1])
            new_line.append(line[2])

            if '조사' in line[-2] and line[-2] != '일반보조사':
                if len(line) > 5:
                    new_line.append(line[-5])
                    new_line.append(line[-4])
                    new_line.append(line[-3])
                    new_line.append(line[-2])
                else:
                    new_line.append('NULL')
                    new_line.append('NULL')
                    new_line.append(line[-3])
                    new_line.append(line[-2])
            else:
                if len(line) > 5:
                    new_line.append(line[-3])
                    new_line.append(line[-2])
                    new_line.append('NULL')
                    new_line.append('NULL')
                else:
                    new_line.append(line[-3])
                    new_line.append(line[-2])
                    new_line.append('NULL')
                    new_line.append('NULL')

            a = '\t\t'.join(new_line)
            f2.write(a + '\n')


## endl
