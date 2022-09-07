# @Author: JY
# @Date:   2019-02-11T09:39:32+09:00
# @Filename: e_18.py
# @Last modified by:   JY
# @Last modified time: 2019-02-11T10:07:37+09:00
# @Copyright: JeeY

filename_00 = 'result_03.result'
filename_01 = 'result_pos_temp_00.pos'

result_list = list()

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
            for y,x in enumerate(line[2:]):
                if y%2 == 1:
                    result_list.append(x)
                    # print(x)

# print(result_list)

with open(filename_01, 'w', encoding='utf-8') as fw:
    for x in result_list:
        fw.write(x + '\n')














## end line
