class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
        
class List:
    def __init__(self):
        self.head = None
        
        
    def tamaño(self):
        contador = 0
        itr = self.head
        
        while itr:
            contador += 1
            itr = itr.next
        print(contador)
        
    def print(self):
        if self.head is None:
            print("The list is empty")
            
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + "-->"if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
        
    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        
    def insert_beging(self,data):
        if self.head is None:
            self.head = None
        
        self.head = Node(data,self.head)
        
        
    def insert_at(self,index,data):
        itr = self.head 
        #if index == 0:
            #insert_beging(data)
        
        
uno = List()
uno.print()
uno.insert_end(7)
uno.insert_end(9)
uno.insert_end(1)
uno.insert_end(15)
uno.insert_beging(0)
uno.insert_beging(0)
uno.print()
uno.tamaño()