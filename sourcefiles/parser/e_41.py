# @Author: J.Y.
# @Date:   2019-02-27T10:50:42+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-02-27T11:20:26+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filename0 = 'temp_result_00.temp'
filename1 = 'temp_result_04.temp'
filename2 = 'temp_result_05.temp'
filename3 = 'temp_result_06.temp'

with open(filename0, 'r', encoding='utf-8') as f, open(filename1, 'w', encoding='utf-8') as f1,\
open(filename2, 'w', encoding='utf-8') as f2, open(filename3, 'w', encoding='utf-8') as f3:
    list0 = list()
    list1 = list()
    list2 = list()
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if '오른열림기호' in line or '왼열림기호' in line:
            list0.append(line)
        if '조사' in line[-1]:
            list1.append(line)

    for i in list1:
        list2.append(i[-1])
    temp = list(set(list2))
    for i in list0:
        line = '\t'.join(i)
        f1.write(line + '\n')

    for i in list1:
        line = '\t'.join(i)
        f2.write(line + '\n')

    for i in temp:
        f3.write(str(i) + '\n')














## endl
