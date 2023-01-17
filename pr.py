#lista ligada

class Node:
	def __init__(self,data,next):
		self.data = data 
		self.next = next         

class LinkedList:

	def __init__(self):
		self.head = None

	def ver(self):
		if self.head is None:
			print("Linked list is empty")

		itr = self.head
		llstr = ''

		while itr:
			llstr += str(itr.data) + '-->' if itr.next else str(itr.data)
			itr = itr.next
		print(llstr)

	def insert_begin(self,data):
		node=Node(data,self.head)
		self.head = node

nueva = LinkedList()
nueva.insert_begin(2)
nueva.insert_begin(4)
nueva.insert_begin(7)
nueva.ver()