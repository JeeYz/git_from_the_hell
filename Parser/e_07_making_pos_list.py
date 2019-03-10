# @Author: JY
# @Date:   2019-01-25T16:25:31+09:00
# @Filename: e_07.py
# @Last modified by:   JY
# @Last modified time: 2019-01-25T16:59:59+09:00
# @Copyright: JeeY


filename_00 = 'pos_list.pos'
filename_01 = 'result_pos_list.pos'
filename_02 = 'pos_list_01.pos'
filename_03 = 'result_pos_list_01.pos'

result_pos_list = list()

with open(filename_02, 'r', encoding='utf-8') as f1:
    while True:
        line = f1.readline()
        if not line: break
        line = line.split()
        if len(line) == 0: continue
        new_line = []
        new_line.append(line[0])
        new_line.append(''.join(line[1:]))
        result_pos_list.append(new_line)


with open(filename_03, 'w', encoding='utf-8') as f2:
    for i in result_pos_list:
        f2.write(str(i[1]) +'\t\t'+ str(i[0]) +'\n')









## end line
