# @Author: J.Y.
# @Date:   2019-02-26T04:08:05+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-09T23:31:49+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

class word_node():
    def __init__(self):
        self.index = None
        self.word = None
        self.childlist = list()
        self.parent = None

def make_full_initial_raw_dataset(filename0):
    full_dataset = list()
    with open(filename0, 'r', encoding='utf-8') as f:
        switch = 1
        while True:
            line = f.readline()
            if not line: break
            line = line.split()
            if switch == 1:
                one_line = list()
                one_line.append(line)
                switch = 0
                continue
            if line == []:
                switch = 1
                full_dataset.append(one_line)
                continue
            one_line.append(line)
    return full_dataset

def make_dependency_tree(given):
    # print(given)
    head = word_node()
    node_list = list()
    for j,i in enumerate(reversed(given[1:])):
        if j == 0:
            # print(i)
            head.index = i[0]
            head.word = i[2]
            node_list.append(head)
        else:
            node = word_node()
            node.index = i[0]
            node.parent = i[1]
            node.word = i[2]
            for k in node_list:
                if int(i[1]) == int(k.index):
                    k.childlist.insert(0, node)
            node_list.append(node)
    root = word_node()
    root.index = 0
    root.word = 'ROOT'
    root.childlist.insert(0, head)
    return root

def retrieve_tree(curr, word1):
    # print('\t** : ', curr.word, word1, type(curr.word), type(word1))
    if curr.childlist == []:
        if curr.word == word1:
            return [curr, 1]
    elif curr.word == word1:
        return [curr, 1]
    else:
        # print('** : ', curr.word)
        for i in curr.childlist:
            # print('++ : ', i.word, word1)
            ret = retrieve_tree(i, word1)
            # print(ret)
            if ret[1] == 1:
                return ret
    return [None, 0]

def generate_list_1(curr):
    temp = list()
    # print(curr.word)
    if curr.childlist == []:
        temp = ['NULL', "NULL", "NULL", "NULL"]
    else:
        if len(curr.childlist) == 1:
            temp = [curr.childlist[0].word, curr.childlist[0].word, 'NULL', 'NULL']
        else:
            temp = [curr.childlist[0].word, curr.childlist[-1].word, \
            curr.childlist[1].word, curr.childlist[-2].word]
    return temp

def generate_list_2(curr):
    temp = list()
    # print(curr.word)
    if curr.childlist == []:
        return ['NULL', 'NULL']
    else:
        if len(curr.childlist) == 1:
            # print(curr.childlist[0].word)
            if curr.childlist[0].childlist == []:
                return ['NULL', 'NULL']
            else:
                return [curr.childlist[0].childlist[0].word, curr.childlist[0].childlist[-1].word]
        else:
            if curr.childlist[0].childlist == []:
                temp.append('NULL')
            else:
                temp.append(curr.childlist[0].childlist[0].word)
            if curr.childlist[-1].childlist == []:
                temp.append('NULL')
            else:
                temp.append(curr.childlist[-1].childlist[-1].word)
            return temp

def make_one_train_data(stack, buffer, root):
    # print(stack)
    # print(buffer)
    one_data = list()
    for i,j in enumerate(stack):
        if i >= 3:
            break
        one_data.append(j)
    # print('** : ', one_data, i)
    if len(one_data) < 3:
        a = ["NULL" for k in range(3-len(one_data))]
        one_data.extend(a)
    # print('** : ', one_data)
    for i,j in enumerate(buffer):
        if i >= 3:
            break
        one_data.append(j)
    # print('** : ', one_data, i)
    if len(one_data) < 6:
        a = ["NULL" for k in range(6-len(one_data))]
        one_data.extend(a)
    # print('** : ', one_data)
    #########debuging sessino#################
    if len(one_data) != 6:
        print('\t', '***** : ', one_data)
    ##########################################
    for i in range(2):
        if one_data[i] == 'NULL':
            one_data.extend(["NULL", "NULL", "NULL", "NULL"])
        else:
            # print(root.word)
            # print(one_data[i])
            position = retrieve_tree(root, one_data[i])
            # print(position)
            tmplist = generate_list_1(position[0])
            # print(tmplist)
            one_data.extend(tmplist)
    # print('** : ', one_data)
    for i in range(2):
        if one_data[i] == 'NULL':
            one_data.extend(["NULL", "NULL"])
        else:
            position = retrieve_tree(root, one_data[i])
            # print(position)
            tmplist = generate_list_2(position[0])
            one_data.extend(tmplist)

    return one_data

def print_tree(curr):
    if curr.childlist == []:
        return
    else:
        for i in curr.childlist:
            print_tree(i)
            (i.index, '\t', i.word, '\t', i.childlist, '\t', i.parent)
            # node_list.append(i)


if __name__ == "__main__":
    print('hello, world~!')
    print("Only Execution of module No.1")
















## endl
