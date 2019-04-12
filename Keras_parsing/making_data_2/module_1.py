# @Author: J.Y.
# @Date:   2019-04-12T04:45:47+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-12T11:01:07+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

fpath = 'd:/Program_Data/Parsing_Data/'

def write_new_divided_train_data(filenum, sents):
    fname = fpath + 'parsing_train_data_%02d.train' %filenum
    with open(fname, 'a', encoding='utf-8') as fw:
        for line in sents:
            fw.write('  '.join(line) + '\n')


if __name__ == '__main__':
    print('hello, world~!')

## endl
