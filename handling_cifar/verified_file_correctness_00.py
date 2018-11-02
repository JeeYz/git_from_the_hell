# @Author: JayY <JeeYz>
# @Date:   2018-11-02T14:25:57+09:00
# @Filename: verified_file_correctness_00.py
# @Last modified by:   JeeYz
# @Last modified time: 2018-11-02T14:55:03+09:00
# @Copyright: JayY

import os

fn_w1 = 'cifar_10_train_'
fn_w2 = 'cifar_test.txt'

for (path, dir, files) in os.walk('./'):
    for filename in files:
        if fn_w1 in filename:
            the_file = path + '/' + filename
            with open(the_file, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline().split()
                    if not line: break
                    if len(line) != 3073:
                        print('hello, ERROR~!~! :)')
                print("hello, world~!   ", "the Operation is done.")
        elif fn_w2 in filename:
            the_file = path + '/' + filename
            with open(the_file, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline().split()
                    if not line: break
                    if len(line) != 3073:
                        print('hello, ERROR~!~! :)')
                print("hello, world~!   ", "the Operation is done.")



''' # this is proto type of this function to verifying
with open('cifar_00.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline().split()
        if not line: break
        if len(line) != 3073:
            print('hello, ERROR~!~! :)')
'''
