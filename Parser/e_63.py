# @Author: J.Y.
# @Date:   2019-03-10T01:09:40+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-10T01:22:17+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

filename0 = 'temp_result_08_v02.temp'
filename1 = 'temp_result_09.temp'

arc_list = list()
with open(filename0, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        if line == []:continue
        if line[-1] not in arc_list:
            arc_list.append(line[-1])

arc_list.sort()
print(arc_list)

with open(filename1, 'w', encoding='utf-8') as f:
    for i in arc_list:
        f.write(str(i) + '\n')














## endl
