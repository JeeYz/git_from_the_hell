# @Author: JayY
# @Date:   2018-11-02T13:10:26+09:00
# @Filename: cifar_dataset_to_text_file_00.py
# @Last modified by:   JeeYz
# @Last modified time: 2018-11-02T14:51:35+09:00
# @Copyright: JayY

import numpy as np
import os

filename_for_writing1 = 'cifar_10_train_'
filename_for_writing2 = 'cifar_test.txt'
file_num = 1

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

for (path, dir, files) in os.walk('./'):
    for filename in files:
        if 'data_batch_' in filename:
            file = path + '/' + filename
            cifar_dict = dict()
            cifar_dict = unpickle(file)
            data_num = len(cifar_dict[b'labels'])
            w_filename = filename_for_writing1 + str("%2d" %file_num) + '.txt'
            file_num += 1
            with open(w_filename, 'w', encoding='utf-8') as f:
                for ij in range(data_num):
                    a = cifar_dict[b'data'][ij]
                    b = " ".join(str(v) for v in a)
                    c = cifar_dict[b'labels'][ij]
                    f.write(str(c) + ' ' + b + '\n')
            print('hello, coding~!@@', '\t', 'operation for create file ', w_filename)
        elif filename == 'test_batch':
            file = path + '/' + filename
            cifar_dict = dict()
            cifar_dict = unpickle(file)
            data_num = len(cifar_dict[b'labels'])
            w_filename = filename_for_writing2
            with open(w_filename, 'w', encoding='utf-8') as f:
                for ij in range(data_num):
                    a = cifar_dict[b'data'][ij]
                    b = " ".join(str(v) for v in a)
                    c = cifar_dict[b'labels'][ij]
                    f.write(str(c) + ' ' + b + '\n')
            print('hello, coding~!@@', '\t', 'operation for create file ', w_filename)


''' # this was occured error causing type
for ij in range(data_num):
    a = cifar_dict[b'data'][ij]
    b = " ".join(str(v) for v in a)
    c = cifar_dict[b'labels'][ij]
    fp.write(str(c) + ' ' + b + '\n')
'''



'''
for ij in range(data_num):
    fp.write(str(cifar_dict[b'labels'][ij]) + ' ' + str(cifar_dict[b'data'][ij]) + '\n')
'''



'''
for label in cifar_dict[b'labels']:
    data = str('')
    for i in cifar_dict[b'data']:
        data += str(i) + ' '
    fp.write(str(label) + ' ' + str(data) + '\n')
'''



'''
print(cifar_dict[b'batch_label'])

para_num = 0

for i in cifar_dict[b'data']:
    print(i)
'''



'''
for i in cifar_dict[b'labels']:
    print(i)
'''



'''
for num in cifar_dict:
    fp.write(str(num))
    fp.write('\n')
'''



'''
with open('./cifar-10-batches-py/data_batch_1', 'rb') as f:
    byte = f.read()
    print(byte)
'''
