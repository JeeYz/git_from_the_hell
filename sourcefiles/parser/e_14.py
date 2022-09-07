# @Author: JY
# @Date:   2019-01-30T15:24:27+09:00
# @Filename: e_14.py
# @Last modified by:   JY
# @Last modified time: 2019-01-31T09:44:55+09:00
# @Copyright: JeeY

filename0 = 'result_temp_sentence_00.sentence'
filename1 = 'result_temp_sentence_01.sentence'
filename2 = 'result_raw_words_list_temp_with_freq.words'
filename3 = 'result_raw_words_list_temp_with_freq_1.words'

padstart = '##$%PAD_START'
padend = '##$%PAD_END'


with open(filename0, 'r', encoding='utf-8') as fr, \
open(filename1, 'w', encoding='utf-8') as fw:
    line_num = 0
    while True:
        line = fr.readline()
        if not line: break
        line = line.split()
        line.insert(0, padstart)
        line.append(padend)
        # print(line)

        wline = ' '.join(line)
        fw.write(str(wline) + '\n')
        line_num +=1

with open(filename2, 'r', encoding='utf-8') as fr, \
open(filename3, 'w', encoding='utf-8') as fw:
    fw.write(str(padstart) + '\t\t'+ str(0) +'\t\t'+ 'PAD' + '\t\t' + str(line_num) + '\n')
    fw.write(str(padend) + '\t\t'+ str(1) +'\t\t'+ 'PAD' + '\t\t' + str(line_num) + '\n')
    num = 2
    while True:
        line = fr.readline()
        if not line: break
        line = line.split()
        # print(line)
        fw.write(str(line[0]) +'\t\t'+ str(num) +'\t\t'+ str(line[1]) + '\t\t' + str(line[2]) + '\n')
        num += 1






## endl
