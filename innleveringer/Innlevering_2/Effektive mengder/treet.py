import sys
# class Treet:
#     def __init__(self):
#         self.size = 0
#         self.forste = None
#         self.siste = None
        
#     def contains(self,tall):
#         pass
#     def insert(self,tall):
#         pass
#     def remove(self, tall):
#         pass

import sys

class Node:
    def __init__(self, element):
        # self.barn = None
        # self.forelder = None
        self.left = None
        self.right = None
        self.element = element

class Set:
    def __init__(self):
        self.foerste = None
        self.size = 0

    # def dybde(self, v):
    #     # ny_node = Node(v)
    #     if v == None:
    #         return -1
    #     return 1 + self.dybde(v.forelder) 
    
    # def hoyden(self, v):
    #     h =-1
    #     if v == None:
    #         return h
    #     for c in v.barn:
    #         h = max(h,self.hoyden(c)) 
    
    # def preorder(self,v):
    #     if v == None:
    #         return
    #         # operate on v
    #     for c in v.children:
    #         self.preorder(c)

    # def postorder(self,v):
    #     if v == None:
    #         return
    #     for c in v.children:
    #         self.preorder(c)        
    #         # operate on v

    # def insert_t(self, v, x):
    #     if v == None:
    #         v = Node(x)
    #     elif x < v.element:
    #         v.left = self.insert_t(v.left, x)
    #     elif x > v.element:
    #         v.right = self.insert_t(v.right, x)
    #     return v
    def insert():
        pass
    
    def search_t(self, v, x):
        if v == None:
            return None
        if v.element == x:
            return v
        if x < v.element:
            return self.search_t(v.left, x)
        if x > v.element:
            return self.search_t(v.right, x)
    
    def findMin(v):
        if v == None:
            return None
        
    
    def contains(self,tall):
        pass
    def insert(self,tall):
        pass
    def remove(self, tall):
        pass


treet = Set()

for linje in sys.stdin:
    elementer = linje.split()
    if elementer[0] == "push_front":
        treet.push_front(elementer[1])
    elif elementer[0] == "push_back":
        treet.push_back(elementer[1])
    elif elementer[0] == "push_middle":
        treet.push_middle(elementer[1])
    elif elementer[0] == "get":
        treet.get(int(elementer[1]))
