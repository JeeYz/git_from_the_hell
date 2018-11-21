# @Author: JayY
# @Date:   2018-11-20T16:24:47+09:00
# @Filename: generating_raw_data_from_korean_news_02.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-21T11:44:35+09:00
# @Copyright: JayY

# failure
# ==========================================

filename04 = './data/korean_news/korean_news_result_words_00.txt'
filename05 = './data/korean_news/korean_news_result_sents_00.txt'
filename06 = './data/korean_news/korean_news_result_sents_01.txt'
filename07 = './data/korean_news/korean_news_result_words_01.txt'
filename08 = './data/korean_news/korean_news_result_words_02.txt'
filename09 = './data/korean_news/korean_news_result_poses_list.txt'

def make_poses_list(filename_r, filename_w):
    with open(filename_r, 'r', encoding='utf-8') as f1, open(filename_w, 'w', encoding='utf-8') as f2:
        line_para = 0
        pausing_lines = 100
        pos_list = list()
        while True:
            line = f1.readline().split()
            if not line: break
            if line[1] not in pos_list:
                pos_list.append(line[1])
            if len(line) != 2:
                print(line)
        pos_list = sorted(pos_list)
        for pos in pos_list:
            f2.write(str(pos) + '\n')
        return pos_list

def reducing_duplicated_words(filename_r, filename_w):
    temp_word_dict = dict()
    pos_list = list()
    para = 0
    with open(filename_r, 'r', encoding='utf-8') as f1, open(filename_w, 'w', encoding='utf-8') as f2:
        while True:
            line = f1.readline().split()
            if not line: break
            if line[1] not in pos_list:
                pos_list.append(line[1])
            if line[0] in temp_word_dict:
                temp_word_dict[line[0]][1] += 1
            else:
                temp_word_dict[line[0]] = [line[1], 1]
            para += 1
            if para%100000==0:
                print('hello, world   ', para)

        for word in temp_word_dict:
            f2.write(str(word) + '\t' + str(temp_word_dict[word][0]) + '\t' + str(temp_word_dict[word][1]) + '\n')

reducing_duplicated_words(filename04, filename07)
