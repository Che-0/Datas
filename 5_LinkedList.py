class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
    
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--> '
            itr = itr.next
        print(llstr)

ll = LinkedList()
ll.insert_at_begining(2)
ll.insert_at_begining(3)
ll.insert_at_begining(4)
ll.print()