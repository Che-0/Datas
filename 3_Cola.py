#Cola

class queue:
    def __init__(self):    #crea una colar cuando se intancia un objeto
        self.top = 0       #posicion 0
        self.queue = []    #cracion de la cola

    def encolate(self,valor):    #agregar valor a la cola
        self.queue.append(valor) 

    def dequeue(self):           #eliminar el valor de la cola(el primero [0] que es top)
        self.queue.pop(self.top)

    def front(self):             #imprime el valor de la posicion 0
        print("El primer elemento es:")
        print(self.queue[self.top])

    def __str__(self):        #imprimir pila
        return str(self.queue)

    def __len__(self):        #longitud de la fila
        return len(self.queue)

cola1 = queue()
cola1.encolate(6)
cola1.encolate(7)
cola1.encolate(8)
cola1.encolate(9)
cola1.dequeue()
cola1.dequeue()
print(cola1.queue)
print(cola1)
cola1.front()