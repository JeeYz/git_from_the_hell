# @Author: JayY
# @Date:   2018-11-22T10:20:17+09:00
# @Filename: generating_raw_data_from_korean_news_07.py
# @Last modified by:   JY
# @Last modified time: 2019-01-30T15:23:40+09:00
# @Copyright: JayY

freq_threshold = 8

filename00 = './data/korean_news/korean_news_result_words_04.txt'
# filename01 = './data/korean_news/korean_news_result_words_05.txt'
filename02 = './data/korean_news/korean_news_result_poses_list.txt'
filename03 = './data/korean_news/korean_news_result_sents_02.txt'
filename04 = './data/korean_news/korean_news_result_poses_list_new.txt'
filename05 = './data/korean_news/korean_news_result_sents_03.txt'

def generate_new_pos_file(filename_r, filename_w):
    with open(filename_r, 'r', encoding='utf-8') as f1, open(filename_w, 'w', encoding='utf-8') as f2:
        while True:
            line = f1.readline().split()
            if not line:break
            new_line = str(line[0]) + '\t' + '##RARE_' + str(line[0])
            f2.write(new_line + '\n')

# generate_new_pos_file(filename02, filename04)

def make_dictionaries(filename_r1, filename_r2):
    word_dict_origin = dict()
    pos_dict = dict()
    with open(filename_r1, 'r', encoding='utf-8') as f1, open(filename_r2, 'r', encoding='utf-8') as f2:
        while True:
            line = f1.readline().split()
            if not line: break
            word_dict_origin[line[0]] = [line[1], int(line[2])]
        while True:
            line = f2.readline().split()
            if not line: break
            pos_dict[line[0]] = line[1]
    return word_dict_origin, pos_dict

word_dict_origin, pos_dict = make_dictionaries(filename00, filename04)

def replace_words_of_sentences_file(filename_r, filename_w, word_dict_origin, pos_dict):
    with open(filename_r, 'r', encoding='utf-8') as f1, open(filename_w, 'w', encoding='utf-8') as f2:
        while True:
            line = f1.readline().split()
            if not line: break
            new_line = list()
            for a_word in line:
                temp_val = word_dict_origin.get(a_word)
                if a_word == '##pad_start' or a_word == '##pad_end':
                    new_line.append(str(a_word))
                elif temp_val[0] == 'SN':
                    new_line.append(pos_dict.get('SN'))
                elif temp_val[0] == 'SL':
                    new_line.append(pos_dict.get('SL'))
                elif temp_val[0] == 'SH':
                    new_line.append(pos_dict.get('SH'))
                elif temp_val[1] < freq_threshold:
                    new_line.append(pos_dict.get(temp_val[0]))
                else:
                    new_line.append(str(a_word))
            f2.write(' '.join(new_line) + '\n')

replace_words_of_sentences_file(filename03, filename05, word_dict_origin, pos_dict)
