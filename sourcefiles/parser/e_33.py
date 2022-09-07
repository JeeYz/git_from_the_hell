# @Author: JeeY
# @Date:   2019-02-22T04:00:07+09:00
# @Last modified by:   JeeY
# @Last modified time: 2019-02-22T04:06:16+09:00
# @License: JY
# @Copyright: JY

filename_02 = 'train_dataset_raw_02.train'

with open(filename_02, 'r', encoding='utf-8') as f:
    max_num = 0
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if len(line) > 20:
            if max_num < len(line):
                max_num = len(line)

    print('*max number is %d' %max_num)



## endl
