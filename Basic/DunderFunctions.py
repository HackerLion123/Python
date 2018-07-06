
#Dunder functions are ones with __ on it. It is used for overloading operators.

#EXAMPLES: __init__,__str__,__add__,__len__ etc

class Number:

	def __init__(self,value,type):
		self.value = int(value)
		self.type  = type

	def __str__(self):
		return value

	def __len__(self):
		if self.type == 'integer' or self.type == 'int':
			return 4
		elif self.type == 'float':
			return 8
		else:
			print("ERROR: Not a number\n")

	def __add__(self,num2):
		pass

num1 = Number(30,'integer')

num1 = Number(60,'integer')

print(len(num1))
print(dir(6))