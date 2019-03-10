# @Author: J.Y.
# @Date:   2019-03-04T12:12:57+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-04T14:19:22+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filename0 = 'temp_result_08_v01.temp'
filename1 = 'temp_result_08_v02.temp'

modified_pos_data = list()
with open(filename0, 'r', encoding='utf-8') as f:
    one_sent = list()
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if line == []:
            modified_pos_data.append(one_sent)
            one_sent = list()
        else:
            if line[-1] == '생략' or line[-1] == '문미기호':
                line.append(line[0])
                one_sent.append(line)
            else:
                a = '_'.join(line)
                line.append(a)
                one_sent.append(line)

print(len(modified_pos_data))

with open(filename1, 'w', encoding='utf-8') as f:
    for i in modified_pos_data:
        for j in i:
            line = '\t\t'.join(j)
            f.write(line + '\n')
        f.write('\n')

print('generating file complete...')









## endl
