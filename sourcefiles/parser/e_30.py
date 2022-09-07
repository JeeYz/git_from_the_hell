# @Author: JY
# @Date:   2019-02-19T10:35:12+09:00
# @Filename: e_30.py
# @Last modified by:   JY
# @Last modified time: 2019-02-19T10:42:53+09:00
# @Copyright: JeeY

import time

filename = 'train_dataset_raw_01.train'

with open(filename, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        line = line.split('#$%')
        if line == ['\n']:
            time.sleep(10000)
        print(line)
        for i in line:
            i = i.split()
            print(i)







## endl
