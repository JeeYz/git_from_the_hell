# @Author: JY
# @Date:   2019-01-30T10:02:11+09:00
# @Filename: e_12.py
# @Last modified by:   JY
# @Last modified time: 2019-01-30T11:21:17+09:00
# @Copyright: JeeY

filename00 = 'result_02.result'

with open(filename00, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        if 'N' == line[0] or\
        '[' == line[0] or\
        '\n' == line[0]:
            continue
        line = line.split()
        print(line)
        if int(line[0]) >= int(line[1]) and int(line[1]) != 0:
            print(line)










## end line
