# @Author: J.Y.
# @Date:   2019-02-27T10:10:01+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-02-27T14:20:52+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filename_0 = 'temp_result_00.temp'
filename_1 = 'temp_result_03.temp'

with open(filename_0, 'r', encoding='utf-8') as f1,\
open(filename_1, 'w', encoding='utf-8') as f2:
    list0 = list()
    list1 = list()
    while True:
        line = f1.readline()
        if not line: break
        line = line.split()
        list0.append(line)

    for i,j in enumerate(list0):
        if len(j)>=3:
            # print(j)
            temp = list()
            temp.append(j[0])
            temp.append(j[-1])
            list1.append(temp)
            # print(temp)
        else:
            list1.append(j)

    for i in list1:
        line = '\t'.join(i)
        f2.write(line + '\n')











## endl
