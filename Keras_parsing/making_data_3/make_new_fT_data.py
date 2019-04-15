# @Author: J.Y.
# @Date:   2019-04-15T13:45:46+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-15T13:52:11+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

f_old = 'D:/Program_Data/fastText/fastText-0.1.0/result/train_fT_00'
f_new = 'D:/Program_Data/fastText/fastText-0.1.0/result/train_fT_new'

with open(f_old, 'r', encoding='utf-8') as fr, open(f_new, 'a', encoding='utf-8') as fw:
    while True:
        line = fr.readline()
        if not line:break
        line = line.split()
        line.insert(0, 'ROOT')
        fw.write('  '.join(line) + '\n')







## endl
