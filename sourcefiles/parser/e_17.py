# @Author: JeeY
# @Date:   2019-02-10T04:22:49+09:00
# @Last modified by:   JY
# @Last modified time: 2019-02-11T09:45:56+09:00
# @License: JY
# @Copyright: JY

filename_00 = 'result_03.result'
filename_01 = 'result_04.result'

with open(filename_00, 'r', encoding='utf-8') as f:
    switch = 1
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if switch == 1:
            switch = 0
            sent = line
            continue
        else:
            if len(line) == 0:
                switch = 1
                continue
            # print(line[0], line[1])
            if line[1] == '0':
                continue
            # print(type(line[0]), type(line[1]))
            if int(line[0]) >= int(line[1]):
                print(line)
                print(sent, '\n\n')














## end line
