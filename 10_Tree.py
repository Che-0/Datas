
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:    # <-- Checamos si hay datos
            if data < self.data:    # <-- Si es menor entonces lo mandamos a la izquierda
                if self.left is None:
                    self.left = Node(data)
                else:                       # <-- Si hay un dato en el nodo entonces
                    self.left.insert(data)  # <-- utilizamos recursividad y lo aplicamos a ese nodo
                
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.right.insert(data)
                
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)

        if self.right:
            self.right.printTree()
        
    def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res

    def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)

    def PostorderTraversal(self, root):

        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()