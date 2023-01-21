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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def ultimo_nodo(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def print_Atras(self):
        if self.head is None:
            print("Empty")
        nodo_final = self.ultimo_nodo()

        itr = nodo_final
        lst = ''
        
        while itr:
            lst += str(itr.data) + "-->"
            itr = itr.prev
        print(lst)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def insertar_principio(self,data):
        if self.head == None:
            node = Node(data,self.head,None)
            self.head = node
        else:
            node = Node(data,self.head,None)
            self.head.prev = node 
            self.head = node

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def insertar_final(self,data):
        if self.head == None:
            node = Node(data,None,None)
            return
        itr = self.head

        while itr.next:
            itr =  itr.next

        itr.next = Node(data,None,itr)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def insertar_en(self,index,data):
        #Aqui va un pedo de si esta en el rango de la lista
        #si esta fuera, ps lo mandamis alv, pero esto es practica y es perfecta

        if index == 0:
            self.insertar_principio(data)
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index -1:
                node = Node(data,itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
        
        #falta el de remover
        #Luego

uno = DLinkedList()
uno.insertar_principio(1)
uno.insertar_principio(2)
uno.insertar_principio(3)
uno.insertar_principio(4)
uno.print_Normal()
uno.print_Atras()