# @Author: J.Y.
# @Date:   2019-03-05T16:48:45+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-20T11:04:25+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

def making_word_elements_list(sent_list):
    word_elements_list = dict()
    for r,j in enumerate(sent_list[1:]):
        word_elements_list[j[2]] = list()
        a, b = list(), list()
        for p,q in enumerate(j[3:]):
            if p%2==0:
                a.append(q)
            else:
                b.append(q)
        word_elements_list[j[2]].append(a)
        word_elements_list[j[2]].append(b)
        word_elements_list[j[2]].append(j[-1])
        word_elements_list[j[2]].append([j[0], j[1]])
    word_elements_list['ROOT'] = list()
    word_elements_list['ROOT'].append(['ROOT', 'ROOT'])
    word_elements_list['ROOT'].append(['ROOT', 'ROOT'])
    word_elements_list['ROOT'].append(0)
    word_elements_list['ROOT'].append([0, 0])
    return word_elements_list

def making_arc_list(file):
    result = list()
    with open(file, 'r', encoding='utf-8') as f:
        one_s = list()
        while True:
            line = f.readline()
            if not line: break
            line = line.split()
            if line == []:
                result.append(one_s)
                one_s = list()
                continue
            one_s.append(line[-1])
    return result

def making_result_data(word_data, elements):
    #########debuging sessino#################
    if len(word_data) != 18:
        print(word_data, '\n\n')
    #########################################
    temp1 = list()
    temp2 = list()
    for s in word_data:
        if s == 'NULL':
            temp1.append(['NULL', 'NULL'])
            temp2.append(['NULL', 'NULL'])
        else:
            temp1.append(elements[s][0])
            temp2.append(elements[s][1])
    temp3 = list()
    for s in word_data[6:]:
        if s == 'NULL':
            temp3.append(['NULL', 'NULL'])
        else:
            temp3.append([elements[s][2]])
    result = list()
    result.extend(temp1)
    result.extend(temp2)
    result.extend(temp3)
    return result

def select_trainsition(stack, element_list, word):
    for i,j in enumerate(stack[:-1]):
        b = element_list[j][3][0]
        c = element_list[j][3][1]
        if stack[0] == word and len(stack) == 2:
            result = list()
            result.append('right')
            result.append(int(b))
            return result

        if i == 0:
            a = element_list[j][3][0]
            continue
        ##
        # print(j, '  :  ', a, '  ', b, '  ', c)
        if int(a) == int(c):
            result = list()
            result.append('left')
            result.append(i)
            return result ## type is list()

    result = list()
    result.append('shift')
    result.append(int(b))
    return result



if __name__ == "__main__":
    print('hello, world~!')
    print("Only Execution of module No.2")







## endl
