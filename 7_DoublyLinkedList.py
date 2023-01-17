#Doubly linked list DLL


# Atributos de la clase al instanciarse
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList():
    def __init__(self):
        head = None      #  <--- Puntero        
    
    def push(self,new_data):     # Insertar un nodo en el inicio
        new_node = Node(new_data)
        new_data.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self,prev_node, new_data):
        if prev_node is None:
            print("The given previous node cannot be Null")
            return
        
        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def append(self,new_data):

        new_node = None(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

        new_node.prev = last

        return
    
    def printList(self, node):
 
        print("\nTraversal in forward direction")
        while node:
            print("{}".format(node.data), end =" ")
            last = node
            node = node.next
 
        print("\nTraversal in reverse direction")
        while last:
            print("{}".format(last.data), end =" ")
            last = last.prev