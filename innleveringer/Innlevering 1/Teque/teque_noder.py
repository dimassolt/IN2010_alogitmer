import sys

class Node:
    def __init__(self, element):
        self.neste = None
        self.forrige = None
        self.element = element

class Teque:
    def __init__(self):
        self.forste = None
        self.siste = None
        self.midten = None
        self.stoerrelse = 0
        
    def push_front(self, tall):

        ny_node = Node(tall)

        if self.stoerrelse == 0: 
            self.forste = ny_node
            self.midten = self.forste
            self.siste = self.forste

        elif self.stoerrelse == 1:
            self.forste = ny_node
            self.forste.neste = self.siste
            self.siste.forrige = self.forste
            self.midten = self.siste

        else:
            self.forste.forrige = ny_node
            ny_node.neste = self.forste
            self.forste = ny_node

        self.stoerrelse +=1

    def push_back(self, tall):

        ny_node = Node(tall)

        if self.stoerrelse == 0:
            self.forste = ny_node
            self.midten = self.forste
            self.siste = self.forste

        elif self.stoerrelse == 1:
            self.siste = ny_node
            self.forste.neste = self.siste
            self.siste.forrige =self.forste
            self.midten = self.siste
        
        else:
            self.siste.neste = ny_node
            ny_node.forrige = self.siste
            self.siste = ny_node

        self.stoerrelse +=1

    def push_middle(self, tall):
        
        ny_node = Node(tall)

        if self.stoerrelse == 0:
            self.forste = ny_node
            self.midten = self.forste
            self.siste = self.forste

        elif self.stoerrelse == 1:
            self.siste = ny_node
            self.forste.neste = self.siste
            self.siste.forrige =self.forste
            self.midten = self.siste

        elif self.stoerrelse == 2:
            self.forste.neste = ny_node
            self.siste.forrige =ny_node
            ny_node.neste = self.siste
            ny_node.forrige = self.forste
            self.midten = ny_node

        else:

            if self.stoerrelse % 2 == 0:
                # ny_node.neste = self.midten.neste
                # self.midten.neste.forrige = ny_node
                # self.midten.neste = ny_node
                # ny_node.forrige = self.midten
                # self.midten = ny_node

                self.midten.forrige.neste = ny_node
                ny_node.forrige = self.midten.forrige
                self.midten.forrige = ny_node

                ny_node.neste = self.midten
                self.midten = ny_node
            else:
                ny_node.neste = self.midten.neste
                self.midten.neste.forrige = ny_node
                self.midten.neste = ny_node
                ny_node.forrige = self.midten
                self.midten = ny_node

                # self.midten.forrige.neste = ny_node
                # ny_node.forrige = self.midten.forrige
                # self.midten.forrige = ny_node

                # ny_node.neste = self.midten
                # self.midten = ny_node

        self.stoerrelse +=1

    def get(self, indeks):
        loper = self.forste
        for i in range(indeks):
            loper = loper.neste

        return loper.element

teque = Teque()            
# indeks = 0
# ant_op = 0
for linje in sys.stdin:

    elementer = linje.split()
    
    # if ant_op < indeks:
    #     exit()
    if elementer[0] == "push_front":
        teque.push_front(elementer[1])
    elif elementer[0] == "push_back":
        teque.push_back(elementer[1])
    elif elementer[0] == "push_middle":
        teque.push_middle(elementer[1])
    elif elementer[0] == "get":
        print(teque.get(int(elementer[1])))           
    # else:
    #     ant_op = int(elementer[0])

    # indeks +=1