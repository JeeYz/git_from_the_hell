# @Author: JayY
# @Date:   2018-11-21T16:22:45+09:00
# @Filename: generating_raw_data_from_korean_news_06.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-21T17:18:47+09:00
# @Copyright: JayY

filename00 = './data/korean_news/korean_news_result_words_02.txt'
filename01 = './data/korean_news/korean_news_result_sents_01.txt'
filename02 = './data/korean_news/korean_news_result_sents_02.txt'
filename03 = './data/korean_news/korean_news_result_words_04.txt'
filename04 = './data/korean_news/korean_news_result_sents_00.txt'


def generate_sentences_file(filename_r, filename_w):
    with open(filename_r, 'r', encoding='utf-8') as f1, open(filename_w, 'w', encoding='utf-8') as f2:
        while True:
            line = f1.readline().split()
            if not line: break
            f2.write('##pad_start' + ' ' + ' '.join(line) + ' ' + '##pad_end' + '\n')

generate_sentences_file(filename04, filename01)

def make_voca_dict(filename_r):
    voca_dict = dict()
    # voca_list = list()
    with open(filename_r, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline().split()
            if not line: break
            voca_dict[line[0]] = [line[1], line[2]]
            # voca_list.append(line[0])
    return voca_dict

voca_dict = make_voca_dict(filename00)
print('hello, voca dict~!~!')

def checking_sentences(filename_r, filename_w, voca_dict):
    line_para = 0
    with open(filename_r, 'r', encoding='utf-8') as f1, open(filename_w, 'w', encoding='utf-8') as f2:
        while True:
            new_line = list()
            line = f1.readline().split()
            if not line:break
            for a_word in line:
                if a_word in voca_dict:
                    new_line.append(a_word)
                else:
                    new_line.append('for_delete')
            print(new_line)
            if 'for_delete' not in new_line:
                f2.write(' '.join(new_line) + '\n')
                line_para += 1
                print('hello, world~!   ', line_para)
    return line_para

num_of_lines = checking_sentences(filename01, filename02, voca_dict)

def modified_pad_freq(voca_dict, num_of_lines):
    voca_dict.get('##pad_start')[1] = num_of_lines
    voca_dict.get('##pad_end')[1] = num_of_lines
    print(voca_dict['##pad_start'][1])
    print(voca_dict['##pad_end'][1])
    print(num_of_lines)
    return voca_dict

voca_dict = modified_pad_freq(voca_dict, num_of_lines)

def regenerate_words_file(filename_w, voca_dict):
    with open(filename_w, 'w', encoding='utf-8') as f:
        for a_word in voca_dict:
            f.write(str(a_word) + '\t' + str(voca_dict[a_word][0]) + '\t' + str(voca_dict[a_word][1]) + '\n')

regenerate_words_file(filename03, voca_dict)
