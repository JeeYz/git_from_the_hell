# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 19:19:50 2018

@author: JeeY
"""

#%%
fp = open("example01.txt", "r")
node_list = list()

#%%
class Node:
    def __init__(self):
        self.word = None
        self.type = None
        self.freq = None
        self.parent = None
        self.left = None
        self.right = None
        self.vect = list()
        self.node_address = None
        

#%%
class Heap_Tree:
    def __init__(self):
        self.root = None
        self.tail = None
        self.huff_tail = None
        self.para = 0   
        self.trace = 0
        self.make_heap_tree()
        
        
    def make_heap_tree(self):
        while True:
            in_line = fp.readline()
            #print(in_line)
            
            if not in_line:
                return
            
            tmp = in_line.split()
            wrd = tmp[0]
            typ = tmp[1]
            frq = int(tmp[2])
            
            curr = self.search_node(self.root)
#            print(self.root)
#            print(curr)
            self.insert_data(curr, wrd, typ, frq)
            
#            if curr is not self.root:
#                print('c: ', curr.parent.word, '  ', 'c.p: ', curr.word)    
                        
            self.adjust_insert(curr)
#            self.adjust_tree(self.root)
            
        
    def insert_data(self, curr, wrd, typ, frq):
        curr.word = wrd
        curr.type = typ
        curr.freq = frq
    
    def search_node(self, curr):
            
        if self.root is None:
            self.root = Node()
            curr = self.root
            node_list.append(curr)
            self.para += 1
            return curr
        
        else:
            if curr.left is None:
                curr.left = Node()
                curr.left.parent = curr                
                return curr.left
            
            elif curr.right is None:
                curr.right = Node()
                curr.right.parent = curr
                return curr.right
            
            else:
                node_list.append(curr.left)
                node_list.append(curr.right)
                self.para += 2
                
                self.trace += 1
                temp = Node()
                temp = node_list[self.trace]

                #print(temp.word)
                return self.search_node(temp)
   
    

    def switch_node(self):
        self.tail = Node()
        self.tail = node_list[self.para - 1]
        
        self.root.word = self.tail.word
        self.root.type = self.tail.type
        self.root.freq = self.tail.freq
        self.tail = None
        
        self.para -= 1
        self.tail = node_list[self.para - 1]
         
    
    def heap_pop(self):
        return_node = Node()
        return_node.word = self.root.word
        return_node.type = self.root.type
        return_node.freq = self.root.freq
        self.switch_node()
        self.adjust_tree(self.root)
        return return_node
        
    
    def adjust_insert(self, curr):
        
        if curr.parent is None:
            return
        
        elif curr is self.root:
            return
        
        else:
#            print(curr.freq, '  ', curr.word)
#            print(curr.parent.freq, '  ', curr.parent.word)
#            print('')
            if curr.freq < curr.parent.freq:
                tmp = Node()
                tmp.word = curr.parent.word
                tmp.type = curr.parent.type
                tmp.freq = curr.parent.freq
                curr.parent.word = curr.word
                curr.parent.type = curr.type
                curr.parent.freq = curr.freq
                curr.word = tmp.word
                curr.type = tmp.type
                curr.freq = tmp.freq
                return self.adjust_insert(curr.parent)
        
    
    def adjust_tree(self, curr):
        
        if curr.left is None:
            return
        
        else:
            if curr.left.freq < curr.right.freq and curr.left.freq < curr.freq:
                tmp = Node()
                tmp.word = curr.left.word
                tmp.type = curr.left.type
                tmp.freq = curr.left.freq
                curr.left.word = curr.word
                curr.left.type = curr.type
                curr.left.freq = curr.freq
                curr.word = tmp.word
                curr.type = tmp.type
                curr.freq = tmp.freq
                return self.adjust_tree(curr.left)
            
            elif curr.right.freq < curr.left.freq and curr.right.freq < curr.freq:
                tmp = Node()
                tmp.word = curr.right.word
                tmp.type = curr.right.type
                tmp.freq = curr.right.freq
                curr.right.word = curr.word
                curr.right.type = curr.type
                curr.right.freq = curr.freq
                curr.word = tmp.word
                curr.type = tmp.type
                curr.freq = tmp.freq
                return self.adjust_tree(curr.right)
                


#%%
class Huff_Tree(Heap_Tree):
    def __init__(self):
        self.huffroot = None
        self.root = None
        self.tail = None
        self.huff_tail = None
        self.para = 0   
        self.trace = 0
        self.huff_stack = list()
        self.huff_index = 0

        print("hello, world  04")
        self.make_heap_tree()
        print("hello, world  05")
        self.make_huff_tree()
        
        print("hello, world!!")
        
        
    def make_leaf_node(self):
        
        print('\n\n')
        
        node1 = self.heap_pop()
        print('node1: ', node1.word)
        node2 = self.heap_pop()
        print('node2: ', node2.word)
        
        for i in range(self.huff_index):
            temp = self.huff_stack[i]
            if node1.word == temp.word:
                node1 = temp
                print('**node1: ', node1.word)
                break                
            elif node2.word == temp.word:
                node2 = temp
                print('**node2: ', node2.word)
                break

        new_heap_node = Node()
        new_heap_node = self.search_node(self.root)
        new_heap_node.freq = node1.freq + node2.freq
        new_heap_node.word = 'abc_' + str(self.huff_index)
        
        node_list[self.para] = new_heap_node
        self.para += 1
        
        new_huff_node = Node()
        new_huff_node.left = node1
        new_huff_node.right = node2 
        
        new_huff_node.freq = new_heap_node.freq
        new_huff_node.word = 'abc_' + str(self.huff_index)
        
        node1.parent = node2.parent = new_huff_node
        self.huff_stack.append(new_huff_node)
        self.huff_index += 1
        new_huff_node.node_address = new_heap_node
        
        node1.vect.append(0)
        node2.vect.append(1)
        

    def make_huff_tree(self):
        
        for i in range(30):
            self.make_leaf_node()
      
        
#        while True:
#            print('++self.root: ', self.root.word)
#            if self.root is None:
#                break
#            
#            self.make_leaf_node()
#
#            
#        print(self.huffroot.word)
            
        
        
        
        
        
#%%
a = list()

c = Huff_Tree()

#print('\n')

curr = c.root

while curr is not None:
    print(curr.word)
    curr = curr.left





#%%




