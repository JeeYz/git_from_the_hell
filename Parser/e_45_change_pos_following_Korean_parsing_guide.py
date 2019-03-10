# @Author: J.Y.
# @Date:   2019-02-27T16:13:37+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-02-28T16:34:30+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filename0 = 'result_modified_pos_data_02.pos'
filename1 = 'result_modified_pos_data_03.pos'

with open(filename0, 'r', encoding='utf-8') as f1, open(filename1, 'w', encoding='utf-8') as f2:
    while True:
        line = f1.readline()
        if not line: break
        line = line.split()
        line = '\t\t'.join(line)
        f2.write(line + '\n')


















## endl
