
# This is used to add multiple arguments to function in a easy way
def function(*args,**kwargs):
	if args:
		print(args)
	if 'name' in kwargs:
		print("Hello,"+kwargs['name'])

function()

function(1,2,3,4)

function(name='Jack')

class Car:
	def __init__(self,color,mileage,type):
		self.color = color
		self.mileage = mileage
		self.type = type

class BMW:
	"""We can use args and kwargs to get the arguments of super class"""
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.type = 'BMW'