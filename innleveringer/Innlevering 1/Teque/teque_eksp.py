import sys
# from collections import deque

# arr1 = deque([])
# arr2 = deque([])


# def push_front(tall):
#     arr1.appendleft(tall)
#     balanse_arr()
   
# def push_middle(tall):
#     arr1.append(tall)
#     balanse_arr()
    
# def push_back(tall):
#     arr2.append(tall)
#     balanse_arr()
   
# def get(indeks):        
#     if indeks < len(arr1):
#         return arr1[indeks]
#     else:
#         indeks = indeks-len(arr1)
#         return arr2[indeks]
    
# def balanse_arr():
#     while len(arr1) > len(arr2):
#         element = arr1.pop()
#         arr2.appendleft(element)
#     while len(arr1) < len(arr2):
#         element = arr2.popleft()
#         arr1.append(element)

# for linje in sys.stdin:
#     elementer = linje.split()
#     if elementer[0] == "push_front":
#         push_front(elementer[1])
#     elif elementer[0] == "push_back":
#         push_back(elementer[1])
#     elif elementer[0] == "push_middle":
#         push_middle(elementer[1])
#     elif elementer[0] == "get":
#         print(get(int(elementer[1]))) 

# n = int(input().strip())
# for _ in range(n):
#     operation, value = input().strip().split()
#     value = int(value)
    
#     if operation == "push_back":
#        push_back(value)
#     elif operation == "push_front":
#        push_front(value)
#     elif operation == "push_middle":
#        push_middle(value)
#     elif operation == "get":
#        print(get(value))

from collections import deque

class Teque:
    def __init__(self):
        self.front = deque()
        # self.middle = deque()
        self.back = deque()
        
    def push_front(self, x):
        self.front.appendleft(x)
        self._balance()
    
    def push_middle(self, x):
        self.front.append(x)
        self._balance()
    
    def push_back(self, x):
        self.back.append(x)
        self._balance()
    
    def get(self, i):
        if i < len(self.front):
            print(self.front[i])
        # elif i < len(self.front) + len(self.middle):
        #     print(self.middle[i - len(self.front)])
        else:
            print(self.back[i - len(self.front)])
    
    def _balance(self):
        # If middle is bigger than front, move the first element from middle to front
        while len(self.front) > len(self.back):
            element = self.front.pop()
            self.back.appendleft(element)
        while len(self.front) < len(self.back):
            element = self.back.popleft()
            self.front.append(element)

teque = Teque()

for linje in sys.stdin:
    elementer = linje.split()
    if elementer[0] == "push_front":
        teque.push_front(elementer[1])
    elif elementer[0] == "push_back":
        teque.push_back(elementer[1])
    elif elementer[0] == "push_middle":
        teque.push_middle(elementer[1])
    elif elementer[0] == "get":
        teque.get(int(elementer[1]))

# Process each operation
# for _ in range(n):
#     operation, value = input().strip().split()
#     value = int(value)
    
#     if operation == "push_back":
#         teque.push_back(value)
#     elif operation == "push_front":
#         teque.push_front(value)
#     elif operation == "push_middle":
#         teque.push_middle(value)
#     elif operation == "get":
#         teque.get(value)
