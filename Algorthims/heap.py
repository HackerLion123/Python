
class Heap:
	""" 
		Heap datastructure using arraylist
		

		(i*2) + 1  # left node
		(i*2) + 2  # right node
	"""

	def __init__(self,capacity):
		self.capacity = capacity
		self.heap = []

	def hasLeftChild(self,index):
		if self.heap[(index*2)+1]:
			return True
		return False


	def hasRightChild(self,index):
		if self.heap[(index*2)+2]:
			return True
		return False

	def hasParent(self,index):
		if index <= 0:
			return False
		return True;

	def parent(self,index):
		return self.heap[index//2];

	def leftchild(self,index):
		if hasLeftChild():
			return self.heap[(index*2)+1]

	def rightchild(self,index):
		if hasRightChild():
			return self.heap[(index*2)+2]

	def swap(self,a,b):
		(self.heap[a],self.heap[b]) = (self.heap[b],self.heap[a])

	def peek(self):
		return self.heap[0]


	def insert_element(self,ele):
		if len(self.heap) <= self.capacity:
			self.heap.append(ele)
		self.heapify();
		
	def delete_element(self):
		ele = self.heap[0]
		self.heap[0] = self.heap[-1]
		del self.heap[-1]
		self.heapify();
		return ele

	def heapify(self):
		index = len(self.heap) - 1;
		while self.hasParent(index) and self.parent(index) < self.heap[index]:
			self.swap(index//2,index)
			index = index//2;

	def sort(self,array):
		for a in array:
			self.insert_element(a)
		self.heapify()
		print(self.peek())
		size = len(self.heap)
		while size>1:
			print(self.delete_element())
			self.heapify()
			size = len(self.heap)

	def heapifyDown(self):
		index = 0
		while hasLeftChild(index):
			if  

	def display(self):
		for ele in self.heap:
			print(ele)

h = Heap(10) # size of heap is 10 if not mentioned it will scale up to any size

# h.insert_element(5)
# h.insert_element(6)
# h.insert_element(8)
# h.insert_element(12)
# h.insert_element(27)
# h.insert_element(21)
# h.insert_element(11)

h.sort([1,2,45,6])
