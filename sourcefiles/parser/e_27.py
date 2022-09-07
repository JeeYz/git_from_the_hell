# @Author: JY
# @Date:   2019-02-18T14:29:16+09:00
# @Filename: e_27.py
# @Last modified by:   JY
# @Last modified time: 2019-02-18T16:15:21+09:00
# @Copyright: JeeY

filename_00 = 'result_raw_words_list_00.words'
filename_01 = './result/output_fasttext_03_dim128.vec'

result_words_list_00 = dict()
result_words_list_01 = dict()

with open(filename_00, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        result_words_list_00[line[0]] = line[0]

with open(filename_01, 'r', encoding='utf-8') as f:
    switch = 1
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if switch == 1:
            switch = 0
            continue
        result_words_list_01[line[0]] = line[0]

compare_words_list_00 = list()
compare_words_list_01 = list()

for i in result_words_list_00:
    if i not in result_words_list_01:
        compare_words_list_00.append(i)

for j in result_words_list_01:
    if i not in result_words_list_00:
        compare_words_list_01.append(i)

print(len(compare_words_list_00), len(compare_words_list_01))
# print(compare_words_list_00)
# print(compare_words_list_01)










## endl
