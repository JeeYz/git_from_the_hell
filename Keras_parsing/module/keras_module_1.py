# @Author: J.Y.
# @Date:   2019-03-22T09:55:52+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-27T14:20:18+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import os

def generate_file_list(path, word_for_target):
    filelist = list()
    for (path, dir, files) in os.walk(path):
        for filename in files:
            if word_for_target in filename:
                filelist.append(filename)
    filelist = tuple(filelist)
    return filelist









if __name__ == "__main__":
    print('hello, world~!!')

## endl
