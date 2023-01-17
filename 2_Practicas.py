#stack

class stack:
    def __init__(self):
        self.top = None
        self.stack = []

    def añadir(self,valor):
        self.top = valor
        self.stack.append(valor)

st1 = stack()
st1.añadir(4)
print(st1.stack)