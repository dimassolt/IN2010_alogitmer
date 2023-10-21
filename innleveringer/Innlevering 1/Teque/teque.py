import sys
from collections import deque
class Teque():
    def __init__(self):
        self.forste = None
        self.arr1 = deque([])
        self.arr2 = deque([])
        self.stoerrelse = 0

    def push_front(self, tall):

        if self.stoerrelse == 0:
            self.forste = tall
            self.arr1.append(tall)

        else:
            self.forste = tall
            self.arr1.appendleft(tall)

        self.balanse_arr()
        self.stoerrelse+=1

    def push_middle(self, tall):
        if self.stoerrelse == 0:
            self.forste = tall
            self.arr1.append(tall)
        else:
            self.arr1.append(tall)
        self.balanse_arr()
        self.stoerrelse += 1

    def push_back(self, tall):

        if self.stoerrelse == 0:
            self.forste = tall
            self.arr1.append(tall)

        else:
            self.arr2.append(tall)

        self.balanse_arr()
        self.stoerrelse+=1

    def get(self, indeks):        
        
        if indeks < len(self.arr1):
            return self.arr1[indeks]
        else:
            indeks = indeks-len(self.arr1)
            return self.arr2[indeks]
        
    def balanse_arr(self):
        while len(self.arr1) > len(self.arr2):
            element = self.arr1.pop()
            self.arr2.appendleft(element)
        while len(self.arr1) < len(self.arr2):
            element = self.arr2.popleft()
            self.arr1.append(element)

teque = Teque()
for linje in sys.stdin:
    elementer = linje.split()
    if "push_front" in linje:
        teque.push_front(elementer[1])
    elif "push_back" in linje:
        teque.push_back(elementer[1])
    elif "push_middle" in linje: 
        teque.push_middle(elementer[1])
    elif "get" in linje:
        print(teque.get(int(elementer[1])))       

