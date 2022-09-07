# @Author: JayY
# @Date:   2018-11-21T15:56:03+09:00
# @Filename: generating_raw_data_from_korean_news_05.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-21T16:05:36+09:00
# @Copyright: JayY


filename00 = './data/korean_news/korean_news_result_words_01.txt'
filename01 = './data/korean_news/korean_news_result_words_02.txt'

def make_voca_dict(filename_r):
    voca_dict = dict()
    with open(filename_r, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline().split()
            if not line: break
            voca_dict[line[0]] = [line[1], line[2]]
    return voca_dict

voca_dict = make_voca_dict(filename00)
voca_tuple = sorted(voca_dict.items())

def modified_voca_dict_and_generate_file(filename_w, voca_tuple):
    with open(filename_w, 'w', encoding='utf-8') as f:
        write_switch = 0
        for a_tuple in voca_tuple:
            if a_tuple[0] == '!':
                write_switch = 1
            if a_tuple[0] == '힝힝':
                f.write(str(a_tuple[0]) + '\t' + str(a_tuple[1][0]) + '\t' + str(a_tuple[1][1]) + '\n')
                write_switch = 0
            if write_switch == 1:
                f.write(str(a_tuple[0]) + '\t' + str(a_tuple[1][0]) + '\t' + str(a_tuple[1][1]) + '\n')

modified_voca_dict_and_generate_file(filename01, voca_tuple)
