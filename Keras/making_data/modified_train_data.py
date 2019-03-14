# @Author: J.Y.
# @Date:   2019-03-14T14:36:55+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-15T07:21:29+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

fpath = 'd:/Program_Data/'
filename0 = 'raw_train_dataset_06.train'
filename1 = 'raw_train_dataset_07.train'

with open(fpath + filename0, 'r', encoding='utf-8') as f1,\
open(fpath + filename1, 'a', encoding='utf-8') as f2:
    while True:
        line = f1.readline()
        if not line:break
        line = line.split()
        if line == []:
            f2.write('\n')
            continue
        num1 = 0
        new_line = list()
        for i in line:
            if i == '##':
                num1 += 1
                new_line.append(i)
                if num1 >= 36:
                    break
                continue
            new_line.append(i)
        new_line.append(line[-1])
        a = '\t'.join(new_line)
        f2.write(a + '\n')







## endl
