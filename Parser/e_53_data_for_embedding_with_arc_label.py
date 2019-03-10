# @Author: J.Y.
# @Date:   2019-03-04T12:21:30+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-04T14:23:06+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

filename0 = 'result_01_arc_labels.sentence'
filename1 = 'temp_result_08_v02.temp'

full_sent_data = list()
with open(filename1, 'r', encoding='utf-8') as f:
    one_sent = list()
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if line == []:
            full_sent_data.append(one_sent)
            one_sent = list()
        else:
            one_sent.append(line[-1])

with open(filename0, 'w', encoding='utf-8') as f:
    for i in full_sent_data:
        line = '  '.join(i)
        f.write(line + '\n\n')








## endl
