# @Author: J.Y.
# @Date:   2019-02-27T15:40:29+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-03T21:59:17+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filename0 = 'temp_result_07.temp'
filename1 = 'result_pos_temp_01.pos'
filename2 = 'result_modified_pos_data_04.pos'
filename3 = 'result_modified_pos_data_05.pos'

with open(filename2, 'r', encoding='utf-8') as f1, open(filename3, 'w', encoding='utf-8') as f2:
    modified_pos = list()
    while True:
        line = f1.readline()
        if not line: break
        line = line.split()
        input_str = input(line[4] + ' : ')
        line.append(input_str)
        line = '\t\t'.join(line)
        f2.write(line + '\n')

















## endl
