# @Author: J.Y.
# @Date:   2019-03-19T20:34:47+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-20T11:23:01+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import time

filename1 = 'd:/Program_Data/raw_train_dataset_08.train'
filename2 = 'd:/Program_Data/raw_train_dataset_07.train'
filename3 = 'd:/Program_Data/raw_train_dataset_06.train'
filename4 = 'd:/Program_Data/raw_train_dataset_05.train'

def check_file_no_8():
    with open(filename1, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []: continue
            if len(line) != 109:
                print(line)
            # print(len(line))

def check_file_no_6():
    with open(filename3, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []: continue
            print(line)
            # print(len(line))

def check_file_no_5():
    with open(filename4, 'r', encoding='utf-8') as f:
        switch = 0
        num1 = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                switch = 0
                num1 = 0
                continue
            if num1 == 0:
                num1 += 1
                continue
            if len(line) != 7:
                print(line)
            # print(len(line))
            num1 += 1

def check_file_no_6_2():
    with open(filename3, 'r', encoding='utf-8') as f:
        para = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []: continue
            if line.count('##') != 48:
                print(line)
            para += 1
            if para == 100:
                time.sleep(10000)


def check_file_no_7():
    with open(filename2, 'r', encoding='utf-8') as f:
        para = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []: continue
            if line.count('##') != 36:
                print(line)
            if len(line) != 109:
                print(para+1)
                print(line)
            para += 1
            # if para == 100:
            #     time.sleep(10000)



# check_file_no_5()
# check_file_no_6()
# check_file_no_6_2()
# check_file_no_7()
check_file_no_8()






## endl
