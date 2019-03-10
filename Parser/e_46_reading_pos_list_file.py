# @Author: J.Y.
# @Date:   2019-02-27T16:16:02+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-04T10:13:52+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filename0 = 'result_modified_pos_data_05.pos'

temp = list()
with open(filename0, 'r', encoding='utf-8') as f1:
    while True:
        line = f1.readline()
        if not line: break
        line = line.split()
        temp.append(line[5])

temp = list(set(temp))
temp.sort()
print(len(temp))

for i in temp:
    print(i)












## endl
