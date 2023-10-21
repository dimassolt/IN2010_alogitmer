from collections import deque
class Teque:
    def __init__(self):
        self.front = deque()
        self.middle = deque()
        self.back = deque()
        self.st_fr = 0
        self.st_md = 0
        self.st_bk = 0

    def push_front(self, x):
        self.front.appendleft(x)
        self.st_fr += 1
        self._balance()
    
    def push_middle(self, x):
        self.middle.append(x)
        self.st_md += 1
        self._balance()
        
    def push_back(self, x):
        self.back.append(x)
        self.st_bk += 1
        self._balance()
    
    def get(self, i):
        if i <= self.st_fr-1:
            print(self.front[i])
        elif i <= self.st_fr + self.st_md-1:
            print(self.middle[i - len(self.front)])
        else:
            print(self.back[i - len(self.front) - len(self.back)])
    
    def _balance(self):
        # If middle is bigger than front, move the first element from middle to front
        # if self.st_fr == self.st_bk == self.st_md:
        #     pass
        
        # else:
            while self.st_fr < self.st_md:
                self.front.append(self.middle.popleft())
                self.st_fr += 1
                self.st_md -= 1

            while self.st_md < self.st_fr:
                self.middle.appendleft(self.front.pop())
                self.st_fr -= 1
                self.st_md += 1
                
            while self.st_md < self.st_bk:
                self.middle.append(self.back.popleft())
                self.st_md += 1
                self.st_bk -= 1

            while self.st_bk < self.st_md:
                self.back.appendleft(self.middle.pop())
                self.st_md -= 1
                self.st_bk += 1







            # If back is bigger than middle, move the first element from back to middle



            
            # while self.st_fr > self.st_bk:
            #     self.back.append(self.front.pop())
            #     self.st_fr -= 1
            #     self.st_bk += 1

# Read the number of operations
n = int(input().strip())

# Initialize a Teque
teque = Teque()

# Process each operation
for _ in range(n):
    operation, value = input().strip().split()
    value = int(value)
    
    if operation == "push_back":
        teque.push_back(value)
    elif operation == "push_front":
        teque.push_front(value)
    elif operation == "push_middle":
        teque.push_middle(value)
    elif operation == "get":
        teque.get(value)
# print(teque.front)
# print(teque.middle)
# print(teque.back)
