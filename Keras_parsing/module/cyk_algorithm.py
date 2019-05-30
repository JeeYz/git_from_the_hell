# @Author: J.Y.
# @Date:   2019-05-27T10:29:01+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-30T14:54:27+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np
import time
import copy


class CYK_table(length, result_matrix):
    def __init__(self):
        self.sent_length = length
        self.main()

    def main(self):
        table = make_cyk_table()
        for i in range(1, len(self.sent_length)):
            for j in reversed(range(i, len(self.sent_length)):
                for k in range(1, i):
                    generate_nodes()
                    pass

    def generate_nodes(self):
        pass

    def make_cyk_table(self):
        table = list()
        table = np.zeors((self.sent_length, self.sent_length))
        return table

    def select_max_value(self):

        pass


class CYK_one_node():
    def __init__(self):
        self.first_score = list()
        self.second_score = list()
        self.arc_score = list()

    def main(self):

        pass





if __name__ == '__main__':
    print('hello, world~!')


## endl
