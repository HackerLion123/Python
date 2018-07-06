
class Duck:

	def __init__(self):
		pass

	def quack(self):
		print("quack quack quack!")

	def fly(self):
		print("fly fly fly")


class Person:

	def __init__(self):
		pass

	def quack(self):
		print("quack like a Duck!")

	def fly(self):
		print("flap hands like a duck")


def quack_and_fly(thing):

	# Non pythonic way
	# if isinstance(thing,Duck):
	# 	thing.quack()
	# 	thing.fly()
	# else:
	# 	print("It is not a Duck")

	# # Non pythonic way
	# if hasattr(thing, 'quack'):
	# 	if callable(thing.quack):
	# 		thing.quack()
	# if hasattr(thing, 'fly'):
	# 	if callable(thing.fly):
	# 		thing.fly()

	# Pythonic way
	try:
		thing.quack()
		thing.fly()
		#thing.bark()
	except AttributeError as e:
		print(e)

def main():
	duck_object = Duck() 
	quack_and_fly(duck_object)

	print

	person_object = Person()
	quack_and_fly(person_object)

if __name__ == '__main__':
	main()

