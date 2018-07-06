# Don't implement stack in python

class Stack:

	def __init__(self):
		stack = []

	def push(self,element):
		stack[stack.length+1] = element

	def pop(self):
		return stack.pop()