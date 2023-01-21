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

    def print_Normal(self):
        if self.head is None:
            print("Empty")
            return
        
        itr = self.head
        lst = ''

        while itr:
            lst += str(itr.data) + "-->" 
            itr = itr.next
        print(lst)


uno = DLinkedList()
uno.print_Normal()