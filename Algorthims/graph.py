class Node:

	def __init__(self,name):
		
		self.name = name

	def getName(self):
		return self.name

class Edge:

	def __init__(self,src,dest):

		self.src = src
		self.dest = dest

	def getSource(self):
		return self.src

	def getDestination(self):
		return self.dest

class Digraph:
	
	def __init__(self):
		pass

	def addNode(self):
		pass

	def addEdge(self):
		pass

	def bfs(self):
		pass

	def dfs(self):
		pass

class Graph(Digraph):

	
