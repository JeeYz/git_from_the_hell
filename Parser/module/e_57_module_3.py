# @Author: J.Y.
# @Date:   2019-03-08T11:11:55+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-15T10:31:56+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

file1 = 'd:/Program_Data/result_raw_words_list_00.words'
file2 = 'd:/Program_Data/result_pos_temp_01.pos'

def making_dictionary_of_words(file):
    words_dict = dict()
    with open(file, 'r', encoding='utf-8') as f:
        index_num = 1
        words_dict['NULL'] = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            words_dict[line[0]] = index_num
            index_num += 1
    return words_dict

def making_pos_dictionary(file):
    pos_dict = dict()
    with open(file, 'r', encoding='utf-8') as f:
        index_num = 1
        pos_dict['NULL'] = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            pos_dict[line[1]] = index_num
            index_num += 1
    return pos_dict

def making_arc_dictionary(file):
    arc_dict = dict()
    with open(file, 'r', encoding='utf-8') as f:
        index_num = 1
        arc_dict['NULL'] = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            arc_dict[line[0]] = index_num
            index_num += 1
    return arc_dict

def return_data_of_words(para):
    words_dict = making_dictionary_of_words(file1)
    pos_dict = making_pos_dictionary(file2)
    if para == 1:
        return words_dict
    elif para == 2:
        return words_dict, pos_dict
    # else:
    #     return words_dict, pos_dict, arc_dict









if __name__ == "__main__":
    print('hello, world~!')
    print("Only Execution of module No.3")

## endl
