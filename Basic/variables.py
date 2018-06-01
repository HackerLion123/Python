
""" Python is loosely typed language variable types are dynamically assigned """
def variables():
	a = 1.0 #Float
	print(type(a))

	a = 2  #integer
	print(type(a))

	a = """Hello""" #String
	print(type(a))

	a = "Hello" #String
	print("{0} with double quotes",type(a))

	a = 'Hello' #String
	print("{0} with single quotes",type(a))

def area(radii):
	pi = 22/7
	return pi*(radii**2)

def main():
	variables();
	printf("Area of a circle with radius 5.2 is",area(5.2))

if __name__ == '__main__':
	main()
