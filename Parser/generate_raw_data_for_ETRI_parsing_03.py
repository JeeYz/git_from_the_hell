# @Author: JeeY
# @Date:   2019-02-01T00:34:28+09:00
# @Last modified by:   JY
# @Last modified time: 2019-02-11T09:39:13+09:00
# @License: JY
# @Copyright: JY


# @Author: JY
# @Date:   2019-01-24T10:29:08+09:00
# @Filename: generate_raw_data_for_ETRI_parsing_02.py
# @Last modified by:   JY
# @Last modified time: 2019-02-11T09:39:13+09:00
# @Copyright: JeeY

import time

sleeptime = 360000

file_path_00 = 'd:/Programming/Exercise_RNN/'
file_path_01 = 'd:/Programming/Corpus/'

read_file = '구문구조부착문장.sentence'
result_file = 'result_03.result'

skip_sent_num = ['21742', '2110', '12032', '13132', '16565', '18086',\
                '22414', '39779', '46049', '124595']

full_up_sentence_list = list()
full_down_sentence_list = list()
full_result = list()
full_result_up = list()

def handle_one_sentence (f_r):
    up_sent_dict = dict()
    down_sent_dict = dict()
    sentence_0 = list()
    sentence_1 = list()
    w_switch = 1

    while True:
        line = f_r.readline()
        if 'Sentence No.' in line:
            for num in skip_sent_num:
                if num in line:
                    return None, None, None, None, None
            temp_sent_num = line
        if '-------' in line:
            break

    raw_sentence = f_r.readline()
    sentence_0 = raw_sentence.split()
    len_0 = len(sentence_0)
    f_r.readline()

    line_num_0 = 0
    while True:
        line = f_r.readline()
        if '------' in line:
            break
        line = line.split()
        # print('++ : ', line)
        # print('== : ', line[0])
        # print(up_sent_dict, '\n\n')
        up_sent_dict[line_num_0+1] = list()
        up_sent_dict[line_num_0+1].append(line[0])
        # print(up_sent_dict)
        if len(line) == 1:
            while True:
                line = f_r.readline()
                if '======' in line:
                    return None, None, None, None, None
        if ']+' in line[1]:
            # print(line[1])
            tmp_list = line[1].split(']+')
            # print(tmp_list)
            for j in tmp_list:
                # print(line)
                # time.sleep(sleeptime)
                if j[-1] == ']':
                    if '[[' in j:
                        up_sent_dict[line_num_0+1].append([j[0], j[2:-1]])
                        # print(up_sent_dict[line[0]])
                        time.sleep(sleeptime)
                    else:
                        temp = j[:-1].split('[')
                        # print(temp)
                        up_sent_dict[line_num_0+1].append([temp[0], temp[1]])
                        # print('******* : ', line[0])
                else:
                    if '[[' in j:
                        up_sent_dict[line_num_0+1].append([j[0], j[2:]])
                    else:
                        temp = j.split('[')
                        # print(temp)
                        up_sent_dict[line_num_0+1].append([temp[0], temp[1]])

            # print('\n')
            # print(up_sent_dict)
            # print('\n')
            # time.sleep(sleeptime)

        else:
            # print(line)
            # time.sleep(sleeptime)
            j = line[1]
            if j[-1] == ']':
                if '[[' in j:
                    up_sent_dict[line_num_0+1].append([j[0], j[2:-1]])
                    print(up_sent_dict[line[0]])
                    time.sleep(sleeptime)
                else:
                    temp = j[:-1].split('[')
                    # print(temp)
                    up_sent_dict[line_num_0+1].append([temp[0], temp[1]])
            else:
                if '[[' in j:
                    up_sent_dict[line_num_0+1].append([j[0], j[2:]])
                else:
                    temp = j.split('[')
                    print(temp, line)
                    up_sent_dict[line_num_0+1].append([temp[0], temp[1]])
        # print('* * * * *\n')
        # print(up_sent_dict)
        # print('\n')
        line_num_0 += 1

    if len_0 != line_num_0:
        # print(sentence_0)
        return None, None, None, None, None

    sentence_1 = f_r.readline().split()
    len_1 = len(sentence_1)
    f_r.readline()

    line_num_1 = 0
    while True:
        line = f_r.readline()
        if '======' in line:
            break
        line = line.split()
        down_sent_dict[line[0]] = list()
        down_sent_dict[line[0]].append(line[1])
        # print(line)
        # time.sleep(sleeptime)

        if ']+' in line[2]:
            tmp_list = line[2].split(']+')
            # print(tmp_list)
            for j in tmp_list:
                if j[-1] == ']':
                    if '[[' in j:
                        down_sent_dict[line[0]].append([j[0], j[2:-1]])
                        print(down_sent_dict[line[0]])
                        time.sleep(sleeptime)
                    else:
                        # print(type(j))
                        # if j.count('[') > 1:
                        #     print(j)
                        temp = j[:-1].rsplit('[', 1)
                        if len(temp) > 2:
                            print(temp)
                        # print(temp)
                        down_sent_dict[line[0]].append([temp[0], temp[1]])
                else:
                    if '[[' in j:
                        down_sent_dict[line[0]].append([j[0], j[2:]])
                    else:
                        # print(type(j))
                        # if j.count('[') > 1:
                        #     print(j)
                        temp = j.rsplit('[', 1)
                        if len(temp) > 2:
                            print(temp)
                        # print(temp)
                        down_sent_dict[line[0]].append([temp[0], temp[1]])

        else:
            j = line[2]
            if j[-1] == ']':
                if '[[' in j:
                    down_sent_dict[line[0]].append([j[0], j[2:-1]])
                    print(down_sent_dict[line[0]])
                    time.sleep(sleeptime)
                else:
                    # print(type(j))
                    # if j.count('[') > 1:
                    #     print(j)
                    temp = j[:-1].rsplit('[', 1)
                    if len(temp) > 2:
                        print(temp)
                    # print(temp)
                    down_sent_dict[line[0]].append([temp[0], temp[1]])
            else:
                if '[[' in j:
                    down_sent_dict[line[0]].append([j[0], j[2:]])
                else:
                    # print(type(j))
                    # if j.count('[') > 1:
                    #     print(j)
                    temp = j.rsplit('[', 1)
                    if len(temp) > 2:
                        print(temp)
                    # print(temp)
                    down_sent_dict[line[0]].append([temp[0], temp[1]])

        line_num_1 += 1

    if len_1 != line_num_1:
        return None, None, None, None, None

    return up_sent_dict, down_sent_dict, sentence_0, sentence_1, raw_sentence

filename_00 = './' + read_file
with open(filename_00, 'r', encoding='utf-8') as f1:
    num = 0
    while True:
        line = f1.readline()
        if not line: break
        if '=====' in line:
            up_dict, down_dict, up_sent, down_sent, raw_sentence = handle_one_sentence(f1)
            # print(up_sent)
            # print(down_sent)
            # print(up_dict)
            # print(down_dict)

            if up_dict != None and down_dict != None:
                temp = list()
                for i, j in enumerate(up_dict):
                    a = list()
                    a.append(int(i+1))
                    for k, l in enumerate(up_dict[j]):
                        if k == 0:
                            a.append(l)
                        else:
                            b = list()
                            for m in l:
                                b.append(m)
                            a.append(b)
                    temp.append(a)
                # print(temp)

                full_up_sentence_list.append(temp)

                temp = list()
                for i in down_dict:
                    b = list()
                    b.append(int(i))
                    for j, k in enumerate(down_dict[i]):
                        if j == 0:
                            b.append(int(k))
                        else:
                            c = list()
                            for l, m in enumerate(k):
                                if l == 0:
                                    for n in m.split('_'):
                                        c.append(n)
                                else:
                                    c.append(m)
                            b.append(c)
                    temp.append(b)

                full_down_sentence_list.append(temp)
                num += 1

print(num)
unequal_num = 0
for n in range(num-1):
    up_cur = list(full_up_sentence_list[n])
    down_cur = list(full_down_sentence_list[n])
    # print(up_cur)
    up_words = list()
    up_s = list()

    for i in up_cur:
        up_s.append(i[1])
        for k, l in enumerate(i[2:]):
            up_words.append(l)

    # print(up_s)
    # print('\n')
####################################################
    # for i in up_cur:
    #     print('$ : ', i)
    # print('\n')
####################################################
    #
    # for i in up_words:
    #     up_s.append(i[0])

    for x in up_cur:
        if '6.29선언' in x[1] and x[2][0] != '6.29선언':
            for y in range(4):
                del x[2]
            temp = list()
            temp.append('6.29선언')
            temp.append('사건고유명사')
            x.insert(2, temp)
            print(x)
            # time.sleep(sleeptime)

    for x in up_cur:
        test = ['12·12', '숫자수사']
        replace = ['12·12', '사건고유명사']
        if test in x:
            a = x.index(test)
            del x[a]
            x.insert(a, replace)
        if '12·12' in x[1] and x[2][0] == '12':
            for y in range(3):
                del x[2]
            temp = list()
            temp.append('12·12')
            temp.append('사건고유명사')
            x.insert(2, temp)
            print(x)

    for x in up_cur:
        test = ['5·18', '숫자수사']
        replace = ['5·18', '사건고유명사']
        if test in x:
            a = x.index(test)
            del x[a]
            x.insert(a, replace)
        if '5·18' in x[1] and x[2][0] == '5':
            for y in range(3):
                del x[2]
            temp = list()
            temp.append('5·18')
            temp.append('사건고유명사')
            x.insert(2, temp)
            print(x)

    for m,i in enumerate(down_cur):
        if i[2] == ['']:
            for x in down_cur[:m]:
                if down_cur[m][0] < x[1]:
                    x[1] -= 1
            for x in down_cur[m:]:
                x[0] -= 1
                x[1] -= 1
            print('\n')
            for y in down_cur:
                print(y)
            time.sleep(sleeptime)
        if i[2][1] == '긍정지정사':
            b = i[0]
            for j in down_cur:
                if j[0] == (b-1):
                    continue
                else:
                    if b == j[1]:
                        j[1] = j[1]-1

    new_list = list()
    # print('\n')

    for j, i in enumerate(down_cur):
        adding_num = 0
        list_a = list()

        first = int(i[0])
        last = int(i[1])
        # print('first : ', first)
        for q, r in enumerate(i[2:]):
            new = list()
            if len(r) > 2:
                for s in r[:-1]:
                    new = list()
                    new.append(first+adding_num)
                    new.append(first+1+adding_num)
                    temp3 = list()
                    temp3.append(s)
                    new.append(temp3)
                    new_list.append(new)
                    adding_num += 1
            else:
                new = list()
                new.append(first+adding_num)
                new.append(first+1+adding_num)
                temp3 = list()
                temp3.append(r[0])
                if r[1] == '긍정지정사':
                    temp3.append(r[1])
                new.append(temp3)
                new_list.append(new)
                adding_num +=1
        adding_num -= 1
        new_list[-1][1] = last+adding_num

        # print('adding_num : ', adding_num)
        for w,m in enumerate(new_list[:-(adding_num+1)]):
            # print('^^value : ', new_list[-1][0], m[1], first)
            if first < m[1]:
                m[1] += adding_num
        for w,m in enumerate(down_cur[j:]):
            m[0] += adding_num
            m[1] += adding_num

    new_list[-1][1] = 0

####################################################
    # print('\n\n')
    # for z in new_list:
    #     print(z)
    # print('\n')
####################################################

    temp_list = list(new_list)
    new_list = list()
    for i,j in enumerate(temp_list):
        if '긍정지정사' in j[2]: ## I have to use i+1
            # print('** j : ', j, i)
            new_list[-1][1] = j[1]
            if new_list[-1][-1][0] == j[2][0]:
                del new_list[-1][-1]
            for z in j[2:]:
                new_list[-1].append(z)
            for y in temp_list[i:]:
                y[0] -= 1
                y[1] -= 1
            for x in new_list:
                if x[1] > new_list[-1][0]:
                    # print(new_list, i)
                    x[1] -= 1
        else:
            new_list.append(j)
    del temp_list

####################################################
    # print('\n\n')
    # for z in new_list:
    #     print(z)
    # print('\n')
####################################################

    del up_words, down_cur
    new_list_2 = list()
    # abs_num = 0

    a = int()
    b = int()
    for i in up_cur:
        a += len(i[2:])
    for i in new_list:
        b += len(i[2:])
    # print('\n++ : ', a, b, '\n\n')
    if a != b:
        unequal_num += 1
        print('\n', 'skip this sentence__!!!')
        print(up_s, '\n')
        continue
        # time.sleep(sleeptime)


    for i, j in enumerate(up_cur):
        temp = list()
        if len(j[2:]) == len(new_list[0][2:]):
            temp.append(new_list[0][0])
            temp.append(new_list[0][1])
            for x in j[2:]:
                temp.append(x)
            new_list_2.append(temp)
            del new_list[0]

        else:
            anum = len(j[2:])
            head = new_list[0][0]
            while (anum-1):
                anum -= len(new_list[0][2:])
                for y in new_list:
                    y[0] -= 1
                    y[1] -= 1
                tail = new_list[1][1]
                for z in new_list_2:
                    if int(new_list[1][0]) < int(z[1]):
                        z[1] -= 1
                del new_list[0]

            del new_list[0]
            temp.append(head)
            temp.append(tail)
            for x in j[2:]:
                temp.append(x)
            new_list_2.append(temp)

    new_list_2[-1][1] = 0

####################################################
    # print(up_s)
    # for z in new_list_2:
    #     print(z)
    # print('\n')
####################################################

    full_result_up.append(up_s)
    full_result.append(new_list_2)
####################################################
    # print('\n')
    # print('hello, world~!~!  ', n, ' th line complete!!!')
    # print('\n\n\n')
####################################################
    # if '생산관계를' in up_s:
    #     time.sleep(sleeptime)
    # if n == 5:
    #     time.sleep(sleeptime)

print('\n\n\n')
print('unequal # : ', unequal_num)
print('up sent length : ', len(full_result_up))
print('word list lendgth : ', len(full_result))
print('\n\n\n')
# for x,y in enumerate(full_result):
#     print(full_result_up[x])
#     print(y)
#     print('\n')

with open(result_file, 'w', encoding='utf-8') as f:
    for i,j in enumerate(full_result):
        a = ' '.join(full_result_up[i])
        f.write(a + '\n')
        for k in j:
            f.write(str(k[0]) +'\t'+ str(k[1]) +'\t')
            for l in k[2:]:
                b = ' '.join(l)
                f.write(b +'\t')
            f.write('\n')
        f.write('\n')















## endl
