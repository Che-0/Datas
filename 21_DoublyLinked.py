#Aqui va el desmadre de la lista doblemente ligada
#Segunda rama para despues combinarla en la rama principal

class Node:
    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev

class DLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self,data):
        if self.head == None:
            self.head = Node(data,None,None)
        else:
            self.head = Node(data,self.head,None)
    
    def insert_end(self,data):
        
        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None,itr)

    def print(self):

        itr = self.head
        lis = ''

        while itr:
            lis += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print(lis)

    def print_reverse(self):
        itr = self.head
        lis = []

        #while itr:
        #    itr = itr.next
        
        while itr:
            lis += str(itr.data) + '-->' if itr.prev else str(itr.data)
            itr = itr.prev
        print(lis)



uno = DLinkedList()
uno.insert_beginning(4)
uno.insert_beginning(6)
uno.insert_beginning(8)

uno.print()
uno.print_reverse()