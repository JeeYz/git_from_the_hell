# @Author: J.Y.
# @Date:   2019-04-08T02:53:18+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-28T12:46:32+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import numpy as np

def add_in_function(a, b):
    a = a - b
    return a

a = 10
b = 5
a = add_in_function(a,
b)

print(a)

for i,j in enumerate(range(10), 1):
    print("%d th %d \n" %(i,j))


c = np.array([1, 0, 5, 3, 4])
d = np.zeros([5, 6])
d[np.arange(5), c] = 1
print(d)


list1 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [1, 2, 3]]]
list1 = np.array(list1)

list2 = list()
list2 = np.append(list2, [1, 2, 3], axis=-1)
print(list2)
list2 = np.append(list2, [4, 5, 6], axis=0)
print(list2)


print('\n\n')
print(list1.shape)

fname = 'd:/Program_Data/Parsing_Data_BiLSTM/parsing_BiLSTM_train_data_00.train'

word = list()
pos = list()
label = list()
word_all = list()
pos_all = list()
label_all = list()
with open(fname, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        if line == []:
            # word = np.array([word])
            # pos = np.array([pos])
            # word_all.append([word])
            # pos_all.append([pos])
            # word = np.array(word)
            # print(word.shape)
            word_all.append(word)
            pos_all.append(pos)
            new_label = list()
            for i in label:
                new = list()
                for j in range(len(label)):
                    if int(j) == int(i):
                        new.append(float(1))
                    else:
                        new.append(float(0))
                new_label.append(new)
            # new_label = np.array(new_label)
            # label_all.append([new_label])
            label_all.append(new_label)
            word = list()
            pos = list()
            label = list()
            continue
        word.append([line[3], line[4]])
        pos.append([line[5], line[6]])
        label.append(line[1])
# print(word_all)
# time.sleep(100000)
word_all = np.array(word_all)
pos_all = np.array(pos_all)
label_all = np.array(label_all)
print(word_all.shape)

















## endl
