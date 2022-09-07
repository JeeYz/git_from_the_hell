# @Author: JayY
# @Date:   2018-08-16T13:35:35+09:00
# @Filename: new_12.py
# @Last modified by:   JY
# @Last modified time: 2019-01-30T16:27:47+09:00
# @Copyright: JayY

# new_12.py
# complete huffman tree
# Ver. 1.0.0


'''
# huffman tree code
'''
import numpy as np
import copy
import sys
sys.setrecursionlimit(50000)

fp = open("./data/korean_wiki/korean_wiki_result_words_01_after_reducing.txt", "r", encoding='utf-8')
fpw1 = open("./data/korean_wiki/korean_wiki_result_words_02_huff_words.txt", 'w', encoding='utf-8')
fpw2 = open("./data/korean_wiki/korean_wiki_result_words_03_huff_nodes.txt", 'w', encoding='utf-8')

class Node:
    def __init__(self):
        self.word = None
        self.type = None
        self.freq = 0
        self.left = None
        self.right = None
        self.parent = None
        self.path_vector = list()

class Heap_Tree:
    def __init__(self):
        self.root = None
        self.tail = None
        self.now_par = None
        self.address_list = list()
        self.para = 0

    def make_heap_tree(self):
        while True:
            tmp = fp.readline().split()
            if not tmp: break
            wrd = str(tmp[0])
            typ = str(tmp[1])
            frq = int(tmp[2])

            curr_node = Node()
            if self.root is None:
                self.root = Node()
                curr_node = self.root
                self.address_list.append(curr_node)
            else:
                a = int(self.para/2)
                curr_node = self.search_tree(self.address_list[a])
                self.address_list.append(curr_node)

            curr_node.word, curr_node.type, curr_node.freq = wrd, typ, frq
            self.insert_adjust(curr_node, int((self.para-1)/2))

    def search_tree(self, curr):
        if curr.left is None:
            curr.left = Node()
            self.para += 1
            return curr.left
        else:
            curr.right = Node()
            self.para += 1
            return curr.right

    def insert_adjust(self, curr, num): #leaf -> root
        if self.address_list[num].freq > curr.freq:
            self.switch_node(self.address_list[num], curr)
            pnum = int((num-1)/2)
            return self.insert_adjust(self.address_list[num], pnum)

    def adjust_tree(self, curr): #root -> leaf
        if curr.left is None:
            return
        else:
            if curr.right is None:
                if curr.freq > curr.left.freq:
                    self.switch_node(curr, curr.left)
                    return self.adjust_tree(curr.left)
            else:
                if curr.freq > curr.left.freq and curr.right.freq >= curr.left.freq:
                    self.switch_node(curr, curr.left)
                    return self.adjust_tree(curr.left)
                elif curr.freq > curr.right.freq and curr.right.freq <= curr.left.freq:
                    self.switch_node(curr, curr.right)
                    return self.adjust_tree(curr.right)

    def switch_node(self, node1, node2):
        temp = Node()
        temp.word, temp.type, temp.freq, temp.path_vector = node1.word, node1.type, node1.freq, node1.path_vector
        node1.word, node1.type, node1.freq, node1.path_vector = node2.word, node2.type, node2.freq, node2.path_vector
        node2.word, node2.type, node2.freq, node2.path_vector = temp.word, temp.type, temp.freq, temp.path_vector

class Huff_Tree(Heap_Tree):
    def __init__(self):
        self.dic_word = dict()
        self.dic_node = dict()
        self.word_index = 0
        self.node_index = 0
        self.print_para = 0
        self.num = 0
        self.count = 0
        self.huff_root = Node()
        self.huff_stack = list()
        Heap_Tree.__init__(self)
        self.make_heap_tree()
        self.huff_para = 0
        self.tail_num = self.para
        self.make_huff_tree()
        self.make_path_list(self.huff_root, None, None)
        self.make_dict_data(self.huff_root)
        self.write_to_file(self.huff_root)

    def make_path_list(self, curr, par_path, path):
        if curr is self.huff_root:
            par_path = []
        else:
            par_path.append(path)
            curr.path_vector = list(par_path)
            par_path = list(curr.path_vector)
        temp = list(par_path)
        if curr.left is not None:
            self.make_path_list(curr.left, par_path, 0)
        if curr.right is not None:
            par_path = list(temp)
            self.make_path_list(curr.right, par_path, 1)

    def make_huff_tree(self):
        for i in range(self.para):
            if self.tail_num < 2: break
            self.make_leaf_node()
        self.make_last_node()

    def make_dict_data(self, curr):
        if curr.left is None:
            self.dic_word[curr.word] = list()
            self.dic_word[curr.word].append(self.word_index)
            self.word_index += 1
            self.dic_word[curr.word].append(curr.type)
            self.dic_word[curr.word].append(curr.freq)
            self.dic_word[curr.word].append(curr.path_vector)
        else:
            self.dic_node[curr.word] = list()
            self.dic_node[curr.word].append(self.node_index)
            self.node_index += 1
            self.dic_node[curr.word].append(curr.type)
            self.dic_node[curr.word].append(curr.freq)
            self.dic_node[curr.word].append(curr.path_vector)

            self.make_dict_data(curr.left)
            self.make_dict_data(curr.right)

    def write_to_file(self, curr):
        b = list()
        for tmp in self.dic_word.items():
            a = list()
            tmp = list(tmp)
            b.append(tmp[0])
            a.append(tmp[0])
            a.append(tmp[1][0])
            a.append(tmp[1][1])
            a.append(tmp[1][2])
            for i in range(len(tmp[1][3])):
                a.append(tmp[1][3][i])
            fpw1.writelines("%s\t" % item for item in a)
            fpw1.write('\n')

        b.sort()
        c = list()
        for tmp in self.dic_node.items():
            a = list()
            tmp = list(tmp)
            c.append(tmp[0])
            a.append(tmp[0])
            a.append(tmp[1][0])
            a.append(tmp[1][1])
            a.append(tmp[1][2])
            for i in range(len(tmp[1][3])):
                a.append(tmp[1][3][i])
            fpw2.writelines("%s\t" % item for item in a)
            fpw2.write('\n')
        c.sort()

    def make_last_node(self):
        node1, node2, new_node = Node(), Node(), Node()

        if 'wrd' in self.address_list[0].word:
            for j in range(len(self.huff_stack)):
                if self.address_list[0].word is self.huff_stack[j].word:
                    node1 = self.huff_stack[j]
                    self.trans_node(self.address_list[0], self.address_list[1])
                    self.address_list.pop()
                    self.tail_num -= 1
                    break
        else:
            self.trans_node(node1, self.address_list[0])
            self.trans_node(self.address_list[0], self.address_list[1])
            self.address_list.pop()
            self.tail_num -= 1

        if 'wrd' in self.address_list[0].word:
            for j in range(len(self.huff_stack)):
                if self.address_list[0].word is self.huff_stack[j].word:
                    node2 = self.huff_stack[j]
                    break
        else:
            self.trans_node(node2, self.address_list[0])

        new_node.left, new_node.right = node1, node2
        new_node.freq = node1.freq + node2.freq
        new_node.word = 'wrd_' + str(self.huff_para)

        self.huff_para += 1
        self.count = 0

        self.huff_stack.append(new_node)
        self.trans_node(self.address_list[self.tail_num], new_node)
        self.insert_adjust(self.address_list[self.tail_num], int((self.tail_num-1)//2))
        '''++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++'''
        self.huff_root = new_node

    def make_leaf_node(self):
        if self.print_para%100 == 0:
            print('hello, world', self.print_para)
        self.print_para+=1
        node1, node2, new_node = Node(), Node(), Node()
        if self.huff_root.word is None:
            self.trans_node(node1, self.address_list[0])
            self.trans_node(self.address_list[0], self.address_list[self.tail_num])
            self.address_list.pop()
            if (self.tail_num-1)%2==0:
                self.address_list[(self.tail_num-1)//2].left = None
            else:
                self.address_list[(self.tail_num-1)//2].right = None
            self.adjust_tree(self.root)
            self.tail_num -= 1

            self.trans_node(node2, self.address_list[0])
            self.trans_node(self.address_list[0], self.address_list[self.tail_num])
            self.address_list.pop()
            if (self.tail_num-1)%2==0:
                self.address_list[(self.tail_num-1)//2].left = None
            else:
                self.address_list[(self.tail_num-1)//2].right = None
            self.adjust_tree(self.root)
        else:
            if 'wrd' in self.address_list[0].word:
                for j in range(len(self.huff_stack)):
                    if self.address_list[0].word is self.huff_stack[j].word:
                        node1 = self.huff_stack[j]
                        self.trans_node(self.address_list[0], self.address_list[self.tail_num])
                        self.address_list.pop()
                        if (self.tail_num-1)%2==0:
                            self.address_list[(self.tail_num-1)//2].left = None
                        else:
                            self.address_list[(self.tail_num-1)//2].right = None
                        self.adjust_tree(self.root)
                        self.tail_num -= 1
                        del self.huff_stack[j]
                        break
            else:
                self.trans_node(node1, self.address_list[0])
                self.trans_node(self.address_list[0], self.address_list[self.tail_num])
                self.address_list.pop()
                if (self.tail_num-1)%2==0:
                    self.address_list[(self.tail_num-1)//2].left = None
                else:
                    self.address_list[(self.tail_num-1)//2].right = None
                self.adjust_tree(self.root)
                self.tail_num -= 1

            if 'wrd' in self.address_list[0].word:
                for j in range(len(self.huff_stack)):
                    if self.address_list[0].word is self.huff_stack[j].word:
                        node2 = self.huff_stack[j]
                        self.trans_node(node2, self.address_list[0])
                        self.trans_node(self.address_list[0], self.address_list[self.tail_num])
                        self.address_list.pop()
                        if (self.tail_num-1)%2==0:
                            self.address_list[(self.tail_num-1)//2].left = None
                        else:
                            self.address_list[(self.tail_num-1)//2].right = None
                        #print(self.address_list[0].word)
                        self.adjust_tree(self.root)
                        del self.huff_stack[j]
                        break
            else:
                #print(self.address_list[0].word)
                self.trans_node(node2, self.address_list[0])
                self.trans_node(self.address_list[0], self.address_list[self.tail_num])
                self.address_list.pop()
                if (self.tail_num-1)%2==0:
                    self.address_list[(self.tail_num-1)//2].left = None
                else:
                    self.address_list[(self.tail_num-1)//2].right = None
                self.adjust_tree(self.root)

        if (self.tail_num-1)%2==0:
            self.address_list[(self.tail_num-1)//2].left = Node()
            self.address_list.append(self.address_list[(self.tail_num-1)//2].left)
        else:
            self.address_list[(self.tail_num-1)//2].right = Node()
            self.address_list.append(self.address_list[(self.tail_num-1)//2].right)

        new_node.left, new_node.right = node1, node2
        new_node.freq = node1.freq + node2.freq
        new_node.word = 'wrd_' + str(self.huff_para)

        self.huff_para += 1
        self.count = 0

        self.huff_stack.append(new_node)
        self.trans_node(self.address_list[self.tail_num], new_node)
        self.insert_adjust(self.address_list[self.tail_num], int((self.tail_num-1)//2))
        '''++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++'''
        self.huff_root = new_node

    def trans_node(self, n1, n2):
        n1.word, n1.type, n1.freq = n2.word, n2.type, n2.freq
        n1.path_vector = n2.path_vector

########### execution #############
a_huff = Huff_Tree()
