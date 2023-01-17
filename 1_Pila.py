#Pila 

class stack:
    def __init__(self):
        self.top = None    #inicializamos los valores en None
        self.stack = []    #Inicializamos la lista vacia de stack

    def vacia(self):        #ver si la pila contiene valores almaacenados o esta vacia 
        if len(self.stack) <= 0:
            return True
        else:
            return False

    def añadir(self,valor):   #funcion para añadir elemnetos a la pila 
        self.top = valor      #Last in First Out 
        self.stack.append(valor)
        return self.top

    def eliminar(self):       #Eliminar valor
        self.stack.pop()
        self.top = self.stack[-1]  #posicionar apuntador -
        return self.top

    def __str__(self):        #imprimir pila
        return str(self.stack)

    def __len__(self):        #longitud de la fila
        return len(self.stack)


#Ejemplo
pila1 = stack()
pila1.añadir(4)
pila1.añadir(6)
print(pila1.__str__()) #imprimir stack
print(pila1.__len__()) #longitud stack
print(pila1) #lo mismo que el metodo imprimir 
print(pila1.vacia())