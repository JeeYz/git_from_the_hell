# @Author: J.Y.
# @Date:   2019-05-27T10:29:01+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-30T15:51:25+09:00
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
        table = self.make_cyk_table()
        for i in range(1, len(self.sent_length)):
            for j in reversed(range(i, len(self.sent_length)):
                temp_results = list()
                for k in range(1, i):
                    temp_results.append(self.generate_nodes(i, j ,k, table))
                self.select_max_value(temp_results, table)

    def generate_nodes(self, x_val, y_val, len_val, table):
        x = x_val + 1
        a = x - len_val - 1
        b = len_val - 1
        c = y_val - len_val
        # [a, c]
        # [b, y]
        return CYK_one_node(a, c, b, y_val, table[c][y_val], table)

    def make_cyk_table(self):
        table = list()
        table = np.zeors((self.sent_length, self.sent_length))
        return table

    def select_max_value(self):

        pass



class CYK_one_node(a, c, b, y, arc_score, table):
    def __init__(self):
        self.first_score = [a, c, table[a][c]]
        self.second_score = [b, y, table[b][y]]
        self.total_score = table[a][c] + table[b][y] + arc_score
        self.total_list = [self.first_score, self.second_score, [arc_score], self.total_score]





if __name__ == '__main__':
    print('hello, world~!')


## endl
