# @Author: J.Y.
# @Date:   2019-05-27T10:29:01+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-31T16:21:05+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np
import time
import copy


class CYK_table():
    def __init__(self, result_matrix):
        self.sent_length = len(result_matrix)
        self.result_matrix = result_matrix
        self.answer = self.main()



    def main(self):
        stack = list()
        answer = list()
        table = self.make_cyk_table()
        for i in range(1, self.sent_length):
            for j in reversed(range(i, self.sent_length)):
                temp_results = list()
                for k in range(1, i+1):
                    temp_results.append(self.generate_nodes(i, j ,k, table))
                table = self.select_max_value(temp_results, table)

        stack = self.retrieve_table(table)
        answer = self.make_answer(stack, table)
        return self.arrange_answer(answer)



    def arrange_answer(self, answer):
        res = np.zeros(len(answer)).tolist()
        for one in answer:
            res[one[0]] = one[1]
        res[0] = 0
        res.append(0)
        # print(len(answer))
        return res



    def make_answer(self, stack, table):
        answer = list()
        for one_node in stack:
            # print(table[one_node[0]][one_node[1]], print(one_node))
            answer.append(table[one_node[0]][one_node[1]].answer)
        return answer



    def make_stack(self, stack, table):
        for one in stack:
            # print('one : ', one)
            # print('stack : ', stack)
            if one[-1] == 2:
                one[-1] = 1
                x = table[one[0]][one[1]].first_score[0]
                y = table[one[0]][one[1]].first_score[1]
                # print('first : ', x, '          ', y)
                if x != 0:
                    stack.append([x, y, 2])
                    self.make_stack(stack, table)
            # print('one : ', one)
            # print('stack : ', stack)
            if one[-1] == 1:
                one[-1] = 0
                x = table[one[0]][one[1]].second_score[0]
                y = table[one[0]][one[1]].second_score[1]
                # print('second : ', x, '          ', y)
                if x != 0:
                    stack.append([x, y, 2])
                    self.make_stack(stack, table)
            # print(one)
        ## check the stack
        # for i in stack:
        #     if i[-1] != 0:
        #         print(stack)
        #         time.sleep(10000)
        return stack



    def retrieve_table(self, table):
        stack = list()
        size_table = len(table)
        x = size_table-1
        y = size_table-1
        stack.append([x, y, 2])
        stack = self.make_stack(stack, table)
        return stack



    def generate_nodes(self, x_val, y_val, len_val, table):
        x = x_val + 1
        # [a, c]
        a = x - len_val - 1
        c = y_val - len_val
        # [b, y]
        b = len_val - 1
        y = y_val

        arc_val = self.result_matrix[c][y]
        temp = CYK_one_node(a, c, b, y, arc_val, table, x_val)
        return temp



    def make_cyk_table(self):
        table = np.zeros((self.sent_length, self.sent_length))
        table = table.tolist()
        return table



    def select_max_value(self, temp_results, table):
        temp = 0
        for one_node in temp_results:
            if temp == 0:
                temp = copy.deepcopy(one_node)
            else:
                if temp.total_score < one_node.total_score:
                    temp = copy.deepcopy(one_node)
        m = copy.deepcopy(temp.location)
        table[m[0]][m[1]] = copy.deepcopy(temp)
        return table



class CYK_one_node():
    def __init__(self, a, c, b, y, arc_score, table, x):
        self.first_score = [a, c]
        # print(self.first_score)
        self.second_score = [b, y]
        if a == 0:
            t1 = 0.0
        else:
            t1 = float(table[a][c].total_score)
        if b == 0:
            t2 = 0.0
        else:
            t2 = float(table[b][y].total_score)
        self.total_score = t1 + t2 + float(arc_score)
        self.location = [x, y]
        self.answer = [c, y]





if __name__ == '__main__':
    print('hello, world~!')
    temp_result = np.random.uniform(0.0, 1.0, (15, 15))
    # print(temp_result)
    temp_result = temp_result.tolist()
    a = CYK_table(temp_result)
    print(a.answer)
    print(len(a.answer))


## endl
