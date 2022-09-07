# @Author: JY
# @Date:   2019-01-25T15:40:57+09:00
# @Filename: e_06.py
# @Last modified by:   JY
# @Last modified time: 2019-01-28T15:25:25+09:00
# @Copyright: JeeY


filename_00 = 'result_raw_words_list_temp.words'
filename_01 = 'result_raw_words_list_temp_with_freq.words'
filename_02 = 'result_raw_words_list_temp_changed_pos_name_ENG.words'

result_dict = {}
result_list = []

with open(filename_00, 'r', encoding='utf-8') as f1:
    while True:
        line = f1.readline()
        if not line: break
        line = line.split()
        temp = list()
        if_switch = 0

        if line[0] in result_list:
            if result_list.index(line[0]):
                num = result_list.index(line[0])
                if result_list[num+1] == line[1]:
                    result_list[num+2] += 1
            else:
                temp = [line[0], line[1], 1]
                result_list.append(line[0])
                result_list.append(line[1])
                result_list.append(1)
        else:
            result_list.append(line[0])
            result_list.append(line[1])
            result_list.append(1)
        #
        # for i, l in enumerate(result_list):
        #     print(result_list)
        #     if line[0] in l and line[1] in l:
        #         result_list[i][2] += 1
        #         if_switch = 1
        #         break
        #
        # if if_switch == 0:
        #     temp = [line[0], line[1], 1]
        #     result_list.append(temp)

print(result_list)



# with open(filename_01, 'w', encoding='utf-8') as f2:
#     for key in result_dict:
#         f2.write(str(key) +'\t\t\t'+ str(result_dict.get(key)[0]) +'\t\t\t')
#         f2.write(str(result_dict.get(key)[1]) +'\n')







## end line
