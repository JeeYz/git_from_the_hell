# @Author: JayY
# @Date:   2018-08-09T14:13:06+09:00
# @Filename: proto_huff_tree_01.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T16:37:57+09:00
# @Copyright: JayY

# !!!!!!!!!!!!!!! this is not completed. !!!!!!!!!!!!!!!!!!!

'''
Prototype of Huffman Tree
허프만 트리의 프로토 타입입니다.
허프만 트리가 Language Model 내에서 어떻게 쓰일지 완전히 이해 안된 상태에서 만들었기 때문에
필요한 기능들이 없습니다.
'''

#%%
fp = open("example01.txt", "r")


#%%
# 노드 클래스
class Node:
    def __init__(self):
        self.word = None # 노드의 단어
        self.type = None # 단어의 품사
        self.freq = 0 # 단어의 frequency
        self.left = None # 왼쪽 자식 노드의 주소
        self.right = None # 오른쪽 자식 노드의 주소
        self.parent = None # 부모 노드의 주소
        self.vector = list() # 경로 벡터값

#%%
# 힙트리 클래스 만들기
class Heap_Tree:
    def __init__(self):
        self.root = None # 힙 트리의 루트
        self.tail = None # 마지막 힙
        #self.now_par = None
        self.address_list = list() # 힙의 주소를 저장해주는 리스트
        self.para = 0 # 힙에 저장된 갯수
        self.trace = 0 # 힙 탐색을 위한 파라미터
        self.make_heap_tree() # 클래스를 선언 할때 힙트리를 만듦


    def insert_data(self, node, w, t, f):
        node.word = w
        node.type = t
        node.freq = f

    # 루트에서 부터 정돈
    def adjust_tree(self, curr):

        if curr.left is None:
            return

        if curr.left is not None and curr.right is not None:

            if curr.left.freq <= curr.right.freq and curr.left.freq < curr.freq:
                self.switch_node(curr, curr.left)
                return self.adjust_tree(curr.left)

            elif curr.left.freq > curr.right.freq and curr.right.freq < curr.freq:
                self.switch_node(curr, curr.right)
                return self.adjust_tree(curr.right)

        else:
            if curr.left is not None:
                if curr.freq > curr.left.freq:
                    self.switch_node(curr, curr.left)
                    return self.adjust_tree(curr.left)

            elif curr.right is not None:
                if curr.freq > curr.right.freq:
                    self.switch_node(curr, curr.right)
                    return self.adjust_tree(curr.right)


    # 힙에서 두개의 노드에 있는 데이터를 뽑아냄.
    def heap_pop(self, temp_node):
        return_node1 = Node()
        return_node2 = Node()

        self.tail = self.address_list.pop()
        self.address_list.append(self.tail)

        print('root: ', self.root.word)
        print('tail: ', self.tail.word)
        for i in range(len(self.address_list)):
                print(i, ' : ', self.address_list[i].word)
        print('************')

        return_node1.word = self.root.word
        return_node1.type = self.root.type
        return_node1.freq = self.root.freq

        self.switch_node(self.root, self.tail)

        self.address_list.pop()
        print('**root: ', self.root.word, '**tail: ', self.tail.word)
        print(len(self.address_list))

        if len(self.address_list) % 2 == 0:
            self.tail.parent.right = None #######    important!!!
        else:
            self.tail.parent.left = None

        self.tail = None
        self.para -= 1

        self.adjust_tree(self.root)

        self.tail = self.address_list.pop()
        self.address_list.append(self.tail)
        print('**root: ', self.root.word, '**tail: ', self.tail.word)

        return_node2.word = self.root.word
        return_node2.type = self.root.type
        return_node2.freq = self.root.freq

        self.switch_node(self.root, self.tail)
        temp_node = self.address_list.pop()
        print('temp_node: ', temp_node.word)

        if len(self.address_list) % 2 == 0:
            self.tail.parent.right = None #######    important!!!

        else:
            self.tail.parent.left = None

        self.para -= 1

        self.adjust_tree(self.root)

        print('**root: ', self.root.word, '**tail: ', self.tail.word)

        print('root: ', self.root.word)
        print('tail: ', self.tail.word)
        for i in range(len(self.address_list)):
                print(i, ' : ', self.address_list[i].word)
        print('************')

        return return_node1, return_node2, temp_node


    # 힙에서 데이터를 뽑아 낸 후에 힙의 제일 마지막 노드와 바꿈
    def switch_node(self, n1, n2):

        tmp = Node()
        tmp.word = n1.word
        tmp.type = n1.type
        tmp.freq = n1.freq

        n1.word = n2.word
        n1.type = n2.type
        n1.freq = n2.freq

        n2.word = tmp.word
        n2.type = tmp.type
        n2.freq = tmp.freq

        tmp = None


    # 힙트리를 만드는 메인 함수
    def make_heap_tree(self):

        while True:
            a_line = fp.readline()

            if not a_line:
                return

            tmp = a_line.split()
            wrd = tmp[0]
            typ = tmp[1]
            frq = int(tmp[2])

            curr_node = Node()
            curr_node = self.search_tree(self.root)

            self.insert_data(curr_node, wrd, typ, frq)

            if curr_node is not self.root:
                self.adjust_insert(curr_node)

            self.trace = 0


    #삽입을 한 후에 테일에서 부터 루트까지 정돈
    def adjust_insert(self, curr):

        if curr.freq < curr.parent.freq:
            self.switch_node(curr, curr.parent)
            return self.adjust_insert(curr.parent)

    # 힙에 삽입할 위치를 탐색
    def search_tree(self, curr):
        if self.root is None:
            self.root = Node()
            self.address_list.append(self.root)
            self.para += 1
            return self.root

        elif curr.left is None:
            curr.left = Node()
            curr.left.parent = curr
            self.address_list.append(curr.left)
            self.para += 1
            return curr.left

        elif curr.right is None:
            curr.right = Node()
            curr.right.parent = curr
            self.address_list.append(curr.right)
            self.para += 1
            return curr.right

        else:
            self.trace += 1
            return self.search_tree(self.address_list[self.trace])


    # 마지막 남은 두개
    def heap_pop_last(self):
        return_node1 = Node()
        return_node2 = Node()

        return_node1.word = self.root.word
        return_node1.type = self.root.type
        return_node1.freq = self.root.freq

        return_node2.word = self.tail.word
        return_node2.type = self.tail.type
        return_node2.freq = self.tail.freq

        return return_node1, return_node2

#%%
# 허프만 트리 클래쓰
class Huff_Tree(Heap_Tree):
    # 클래쓰 생성자
    def __init__(self):
        self.huff_root = None
        self.huff_stack = list()
        Heap_Tree.__init__(self)
        self.make_huff_tree()

    # 허프만 트리를 만드는 메인 함수
    def make_huff_tree(self):

        huff_num = self.para - 1

        for i in range(huff_num):
            print('+++length: ', len(self.address_list))
            end_node = self.make_leaf_node(i)
            print('++++++++++++++++++++++++++++++++++++++++\n')

        self.huff_root = end_node

    # 허프만 트리르 만들어 가는 과정.
    def make_leaf_node(self, max_j):

        if len(self.address_list) == 2:
            node1, node2 = self.heap_pop_last()

            for i in range(max_j):
                tmp_node = self.huff_stack[i]
                if node1.word == tmp_node.word:
                    node1 = tmp_node
                elif node2.word == tmp_node.word:
                    node2 = tmp_node

            new_huff_node = Node()

            new_huff_node.freq = node1.freq + node2.freq
            new_huff_node.left = node1
            new_huff_node.right = node2
            node1.parent = node2.parent = new_huff_node
            self.huff_stack.append(new_huff_node)
            new_huff_node.word = 'node_' + str(max_j)

            return new_huff_node


        else:

            para_node = Node()
            return_node = Node()
            node1, node2, return_node = self.heap_pop(para_node)

            for i in range(max_j):
                tmp_node = self.huff_stack[i]
                if node1.word == tmp_node.word:
                    node1 = tmp_node
                elif node2.word == tmp_node.word:
                    node2 = tmp_node


            new_huff_node = Node()

            new_huff_node.freq = node1.freq + node2.freq
            new_huff_node.left = node1
            new_huff_node.right = node2
            node1.parent = node2.parent = new_huff_node
            self.huff_stack.append(new_huff_node)
            new_huff_node.word = 'node_' + str(max_j)

            w = new_huff_node.word
            t = new_huff_node.type
            f = new_huff_node.freq

            self.insert_data(return_node, w, t, f)
            self.address_list.append(return_node)

            if self.root is not self.tail:
                self.adjust_insert(return_node)

            self.append_vect_0(node1)
            self.append_vect_1(node2)

            return new_huff_node


    # 재귀로 path list에 값 넣기 왼쪽은 0
    def append_vect_0(self, curr):


        if curr is None:
            return

        if curr.left is None:
            curr.vector.append(0)
            return
        else:
            curr.vector.append(0)
            self.append_vect_0(curr.left)
            self.append_vect_0(curr.right)

    # 재귀로 path list에 값 넣기 오른쪽은 1
    def append_vect_1(self, curr):
        if curr is None:
            return
        if curr.left is None:
            curr.vector.append(1)
            return
        else:
            curr.vector.append(1)
            self.append_vect_1(curr.left)
            self.append_vect_1(curr.right)




#%%

# 실제 실행 문들.
b = Huff_Tree()

asdf = b.root


for i in range(b.para):
    print('i : ', b.address_list[i].word)
#%%


#%%
