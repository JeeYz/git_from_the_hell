# @Author: JY
# @Date:   2019-01-29T09:23:33+09:00
# @Filename: e_09.py
# @Last modified by:   JY
# @Last modified time: 2019-01-29T11:06:50+09:00
# @Copyright: JeeY

filename0 = 'result_raw_words_list_temp.words'
filename1 = 'result_temp_sentence_00.sentence'

result_list = list()
temp = list()
with open(filename0, 'r', encoding='utf-8') as fr:
    while True:
        line = fr.readline()
        if not line: break
        line = line.split()

        if line[1] == '문미기호':
            result_list.append(temp)
            temp = []
        else:
            temp.append(line[0])


with open(filename1, 'w', encoding='utf-8') as fw:
    for sent in result_list:
        line = ' '.join(sent)
        fw.write(str(line) +'\n')






## end line
