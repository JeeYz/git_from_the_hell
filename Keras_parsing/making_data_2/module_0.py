# @Author: J.Y.
# @Date:   2019-04-11T11:14:06+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-11T14:56:08+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

class tree_node:
    def __init__(self, i, w):
        self.index = int(i)
        self.word = w      ## list
        self.children = list()
        self.depend = None

def make_small_dict():
    with open(fname2, 'r', encoding='utf-8') as fr2:
        small_dict = dict()
        switch = 1
        while True:
            line = fr2.readline()
            if not line:break
            line = line.split()
            if switch == 1:
                switch = 0
                continue
            if line == []:
                break
            small_dict[line[3]] = line[4]
            small_dict[line[5]] = line[7]
    return small_dict

def return_stack_buffer(j):
    
    return stack, buffer

def generate_depend_list(d_list):
    return d_list

def generate_one_train_data(line, switch, action_stack):
    new_line = list()
    if siwtch == 1:
        new_line.extend(line[:-1])
        for i in range(12):
            new_line.extend(['NULL', 'NULL', '##'])
        new_line.append(line[-1])
    else:
        pass

    return new_line






if __name__ == '__main__':
    print('hello, world~!')

## endl
