# @Author: J.Y.
# @Date:   2019-03-08T11:11:55+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-08T11:31:40+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

def making_dictionary_of_words(file):
    words_dict = dict()
    with open(file, 'r', encoding='utf-8') as f:
        index_num = 1
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            words_dict[line[0]] = index_num
            index_num += 1
    return words_dict















if __name__ == "__main__":
    print('hello, world~!')
    print("Only Execution of module No.3")

## endl
