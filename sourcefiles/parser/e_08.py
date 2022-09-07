# @Author: JY
# @Date:   2019-01-28T15:25:56+09:00
# @Filename: e_08.py
# @Last modified by:   JY
# @Last modified time: 2019-01-28T16:23:25+09:00
# @Copyright: JeeY


filename_00 = 'result_raw_words_list_temp.words'
filename_01 = 'result_raw_words_list_temp_1.words'
filename_02 = 'result_raw_words_list_temp_with_freq.words'
filename_03 = 'result_raw_words_list_temp_changed_pos_name_ENG.words'

result_dict = {}
result_list = []

# with open(filename_00, 'r', encoding='utf-8') as f1:
#     while True:
#         line = f1.readline()
#         if not line: break
#         line = line.split()
#         temp = '/'.join(line)
#         result_list.append(temp)
#
# with open(filename_01, 'w', encoding='utf-8') as fw:
#     for i in result_list:
#         fw.write(str(i) + '\n')


with open(filename_01, 'r', encoding='utf-8') as fr:
    while True:
        line = fr.readline()
        if not line: break
        line = line[:-1]

        if line in result_dict:
            result_dict[line] += 1
        else:
            result_dict[line] = 1

result_dict = sorted(result_dict.items())
# print(result_dict)

with open(filename_02, 'w', encoding='utf-8') as fw:
    for word in result_dict:
        # print(word)
        line = word[0].split('/')
        fw.write(str(line[0] +'\t\t\t'+ str(line[1]) +'\t\t\t'))
        fw.write(str(word[1]) +'\n')








## end line
