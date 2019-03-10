# @Author: JY
# @Date:   2019-02-12T09:52:29+09:00
# @Filename: e_20.py
# @Last modified by:   JY
# @Last modified time: 2019-02-13T09:45:59+09:00
# @Copyright: JeeY

import time
sleeptime = 1000000

filename_00 = 'result_03.result'
filename_01 = 'result_05.result'

full_result_modified  = list()

with open(filename_00, 'r', encoding='utf-8') as f:
    switch = 1
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if switch == 1:
            temp = list()
            sent_list = list(line)
            temp.append(sent_list)
            switch = 0
            continue
        if line == []:
            full_result_modified.append(temp)
            switch = 1
            continue
        for x,y in enumerate(sent_list):
            if x > 0:
                line = f.readline().split()
            temp_1 = list()
            for w,z in enumerate(line):
                if w == 2:
                    temp_1.append(y)
                temp_1.append(z)
            temp.append(temp_1)

with open(filename_01, 'w', encoding='utf-8') as fw:
    for x,y in enumerate(full_result_modified):
        for a,b in enumerate(y):
            if a == 0:
                wline = ' '.join(b)
                fw.write(wline + '\n')
            else:
                wline = '\t'.join(b)
                fw.write(wline + '\n')
        fw.write('\n')




    # if x == 0:
    #     for w,z in enumerate(y):
    #         print(z)
    #     time.sleep(sleeptime)



















## end line
