# @Author: JayY
# @Date:   2018-10-23T11:45:06+09:00
# @Filename: figure_out_number_of_lines_of_a_file_01.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-08T09:53:19+09:00
# @Copyright: JayY



num_of_train_data = 51200000

f_name = './data/korean_wiki/train_data/korean_wiki_skipgram_traindata_'
f_tail = '.txt'
filename_r = './data/korean_wiki/korean_wiki_result_data_for_training_full.txt'

with open(filename_r, 'r', encoding='utf-8') as f1:
    file_num = 0
    func_button = 1
    while func_button:
        file_name = f_name + str('%03d' %file_num) + f_tail
        with open(file_name, 'w', encoding='utf-8') as f2:
            print('hello, world', file_num)
            for i in range(num_of_train_data):
                if i%10000000 == 0:
                    print('hello, world')
                line  = f1.readline().split()
                if not line:
                    func_button = 0
                    break
                if len(line) <= 2: continue
                f2.write(str(line[0]) + '\t' + line[1] + '\t' + line[2] + '\n')
        file_num += 1
