# @Author: JY
# @Date:   2019-01-31T11:34:12+09:00
# @Filename: e_16.py
# @Last modified by:   JY
# @Last modified time: 2019-01-31T15:24:22+09:00
# @Copyright: JeeY


import time

sleeptime = 360000

filename0 = 'result_raw_words_list_temp_1.words'
result_file = 'result_temp_sentence_01_only_pos.sentence'

padstart = 'PAD_S'
padend = 'PAD_E'

result_list = list()

with open(filename0, 'r', encoding='utf-8') as f:
    temp = list()
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        for i in line:
            a = i.split('/')
        if line == [' ', ' ']:
            print(line, 'hello, world')

        if a[1] == '문미기호':
            temp.append(a[1])
            temp.insert(0, padstart)
            temp.append(padend)
            result_list.append(temp)
            temp = list()
        else:
            temp.append(a[1])

# print(result_list)
with open(result_file, 'w', encoding='utf-8') as f:
    for i in result_list:
        line = ' '.join(i)
        f.write(str(line) + '\n')












## endl
