# @Author: JayY
# @Date:   2018-10-22T13:04:48+09:00
# @Filename: reduce_words_in_dictionary.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T14:52:17+09:00
# @Copyright: JayY




# this file is for reducing words.
# make smaller dictionary than now
# ===========================================



f_res = open('./data/korean_wiki/korean_wiki_result_words_01_after_reducing.txt', 'w', encoding='utf-8')

barometer = 8
ENG_num = 0 # type -> ENGL
NUM_num = 0 # type -> NUMB
KAN_num = 0 # type -> KANJ
RARE_num = 0 # type -> RARE

rare_dict = dict()
with open('./data/korean_wiki/korean_wiki_result_words_00_before_reducing.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline().split()
        if not line: break
        if line[1] == 'SH' or line[1] == 'SN' or line[1] == 'SL':
            if line[1] == 'SL':
                ENG_num += 1
            elif line[1] == 'SN':
                NUM_num += 1
            elif line[1] == 'SH':
                KAN_num += 1
        elif int(line[2]) < barometer:
            if line[1] not in rare_dict:
                rare_dict[line[1]] = 1
            else:
                rare_dict[line[1]] += 1
        else:
            f_res.write(str(line[0]) + '\t' + str(line[1]) + '\t' + str(line[2]) + '\n')

f_res.write('!#$_KANJI_' + '\t' + 'KANJ' + '\t' + str(KAN_num) + '\n')
f_res.write('!#$_NUMBER' + '\t' + 'NUMB' + '\t' + str(NUM_num) + '\n')
f_res.write('!#$_ENGLISH' + '\t' + 'ENGL' + '\t' + str(ENG_num) + '\n')

for i in rare_dict:
    f_res.write('!#$_RARE_'+ str(i) + '\t' + str(i) + '\t' + str(rare_dict[i]) + '\n')
