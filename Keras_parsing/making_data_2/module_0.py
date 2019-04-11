# @Author: J.Y.
# @Date:   2019-04-11T11:14:06+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-12T03:30:46+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import copy

class tree_node:
    def __init__(self, i, w):
        self.index = int(i)
        self.word = w      ## list
        self.children = list()
        self.depend = None

def return_stack_buffer_act_stack(j):
    action_stack = list()
    stack = list()
    buffer = copy.deepcopy(j)
    stack.append(['ROOT', 'ROOT'])
    new = tree_node(int(0), ['ROOT', 'ROOT'])
    for m,n in enumerate(j):
        new = tree_node(int(m), n)
        action_stack.append(new)
    return stack, buffer, action_stack

def find_children_1(one, action_stack):
    temp = list()
    if one == ['ROOT', 'ROOT'] or one == ['NULL', 'NULL']:
        for k in range(4):
            temp.extend(['NULL', 'NULL', '##'])
    else:
        for node in action_stack:
            if node.word == one:
                if node.children == []:
                    for k in range(4):
                        temp.extend(['NULL', 'NULL', '##'])
                else:
                    if len(node.children) == 1:
                        temp.extend(node.children[0])
                        temp.append('##')
                        temp.extend(node.children[0])
                        temp.append('##')
                        temp.extend(['NULL', 'NULL', '##'])
                        temp.extend(['NULL', 'NULL', '##'])
                    else:
                        temp.extend(node.children[0])
                        temp.append('##')
                        temp.extend(node.children[-1])
                        temp.append('##')
                        temp.extend(node.children[1])
                        temp.append('##')
                        temp.extend(node.children[-2])
                        temp.append('##')
    return temp

def find_children_2(one, action_stack):
    temp = list()
    if one == ['ROOT', 'ROOT'] or one == ['NULL', 'NULL']:
        for k in range(2):
            temp.extend(['NULL', 'NULL', '##'])
    else:
        for node in action_stack:
            if one == node.word:
                if node.children == []:
                    for k in range(2):
                        temp.extend(['NULL', 'NULL', '##'])
                else:
                    if len(node.children) == 1:
                        for m in action_stack:
                            if m.word == node.children[0]:
                                if m.children == []:
                                    for k in range(2):
                                        temp.extend(['NULL', 'NULL', '##'])
                                else:
                                    if len(m.children) == 1:
                                        temp.extend(m.children[0])
                                        temp.append('##')
                                        temp.extend(m.children[0])
                                        temp.append('##')
                                    else:
                                        temp.extend(m.children[0])
                                        temp.append('##')
                                        temp.extend(m.children[-1])
                                        temp.append('##')
                    else:
                        for m in action_stack:
                            if m.word == node.children[0]:
                                if m.children == []:
                                    for k in range(2):
                                        temp.extend(['NULL', 'NULL', '##'])
                                else:
                                    if len(m.children) == 1:
                                        temp.extend(m.children[0])
                                        temp.append('##')
                                    else:
                                        temp.extend(m.children[0])
                                        temp.append('##')
                            if m.word == node.children[-1]:
                                if m.children == []:
                                    for k in range(2):
                                        temp.extend(['NULL', 'NULL', '##'])
                                else:
                                    if len(m.children) == 1:
                                        temp.extend(m.children[-1])
                                        temp.append('##')
                                    else:
                                        temp.extend(m.children[-1])
                                        temp.append('##')
    return temp

def generate_one_train_data(line, switch, stack, buffer, action_stack):
    temp = list()
    new_line = list()
    if switch == 1:
        new_line.extend(line[:-1])
        for i in range(12):
            new_line.extend(['NULL', 'NULL', '##'])
        new_line.append(line[-1])
    else:
        new_line.extend(line[:-1])
        one = list()
        for j in line[:6]:
            if j == '##':
                child = find_children_1(one, action_stack)
                # print(child)
                new_line.extend(child)
                one = list()
            else:
                one.append(j)
        one = list()
        for j in line[:6]:
            if j == '##':
                child = find_children_2(one, action_stack)
                # print(child)
                new_line.extend(child)
                one = list()
            else:
                one.append(j)
        new_line.append(line[-1])

    if line[-1] == 'shift':
        stack.insert(0, buffer[0])
        del buffer[0]
    elif line[-1] == 'left':
        temp_depend = list()
        for node in action_stack:
            if node.word == stack[0]:
                node.children.append(stack[1])
            elif node.word == stack[1]:
                temp_depend = stack[0]
        for node in action_stack:
            if node.depend == temp_depend:
                node.depend = int(node.index)
        del stack[1]

    return new_line, stack, buffer, action_stack






if __name__ == '__main__':
    print('hello, world~!')

## endl
