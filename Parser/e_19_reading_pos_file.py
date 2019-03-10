# @Author: JY
# @Date:   2019-02-11T10:08:56+09:00
# @Filename: e_19.py
# @Last modified by:   JY
# @Last modified time: 2019-02-11T10:59:32+09:00
# @Copyright: JeeY

filename_01 = 'result_pos_temp_00.pos'
filename_02 = 'result_pos_temp_01.pos'
filename_03 = 'result_pos_temp_02.pos'

new_list = list()

with open(filename_01, 'r', encoding='utf-8') as f1:
    while True:
        line = f1.readline()
        if not line: break
        line = line.split()
        if line[0] in new_list:
            continue
        new_list.append(line[0])

new_list.sort()

# with open(filename_02, 'w', encoding='utf-8') as f:
#     for x,y in enumerate(new_list):
#         f.write(str(x) + '\t' + y + '\n')













## end line
