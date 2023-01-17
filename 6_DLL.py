#a = [1,3,4,5,6]

#b = iter(a)
#
#print(next(b))
#print(next(b))
#print(next(b))
# for Garbage collection
import gc

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node cannot be Null")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next

        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def print_list(self, node):
        print("\nTraversal in forward direction")
        while node:
            print(f"{node.data}",end=" ")
            node = node.next
    
    def append(self, new_data):
        new_node = Node(new_data)
 
        if self.head is None:
            self.head = new_node
            return
 
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last
        return


    #delete element
    def deleteNode(self, dele):
         
        # Base Case
        if self.head is None or dele is None:
            return
         
        # If node to be deleted is head node
        if self.head == dele:
            self.head = dele.next
 
        # Change next only if node to be deleted is NOT
        # the last node
        if dele.next is not None:
            dele.next.prev = dele.prev
     
        # Change prev only if node to be deleted is NOT
        # the first node
        if dele.prev is not None:
            dele.prev.next = dele.next
        # Finally, free the memory occupied by dele
        # Call python garbage collector
        gc.collect()

uno = LinkedList()

uno.push(2)
uno.push(2)
#uno.print_list(uno.head)
uno.insertAfter(uno.head,8)
uno.print_list(uno.head)