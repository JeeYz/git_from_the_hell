# @Author: JayY
# @Date:   2018-11-21T11:08:44+09:00
# @Filename: generating_raw_data_from_korean_news_03.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-21T15:20:47+09:00
# @Copyright: JayY


# this is for making new sentences file
# adding RARE words

filename00 = './data/korean_news/korean_news_result_words_01.txt'
filename02 = './data/korean_news/korean_news_result_sents_00.txt'
filename03 = './data/korean_news/korean_news_result_sents_01.txt'
filename04 = './data/korean_news/korean_news_result_words_00.txt'
filename05 = './data/korean_news/korean_news_result_poses_list.txt'

def count_number_of_sents(filename_r, filename_w):
    num_para = 0
    with open(filename_r, 'r', encoding='utf-8') as fr, open(filename_w, 'w', encoding='utf-8') as fw:
        while True:
            line = fr.readline().split()
            if not line:break
            new_line = fw.write('##pad_start' + ' '.join(line) + ' ' + '##pad_end' + '\n')
            num_para += 1
    return num_para

num_of_sents = count_number_of_sents(filename02, filename03)

def reducing_duplicated_words(filename_r, filename_w1, filename_w2, num_of_sents):
    word_dict = dict()
    pos_list = list()
    word_dict['##pad_start'] = ['PAD', num_of_sents]
    word_dict['##pad_end'] = ['PAD', num_of_sents]
    with open(filename_r, 'r', encoding='utf-8') as f1, open(filename_w1, 'w', encoding='utf-8') as f2:
        while True:
            line = f1.readline().split()
            if not line:break
            if line[0] not in word_dict:
                word_dict[line[0]] = [line[1], 1]
            else:
                word_dict[line[0]][1] += 1
            if line[1] not in pos_list:
                pos_list.append(line[1])
        for a_word in word_dict:
            f2.write(str(a_word) + '\t' + str(word_dict[a_word][0]) + '\t' + str(word_dict[a_word][1]) + '\n')
    with open(filename_w2, 'w', encoding='utf-8') as f:
        for pos in pos_list:
            f.write(str(pos) + '\n')

reducing_duplicated_words(filename04, filename00, filename05, num_of_sents)
