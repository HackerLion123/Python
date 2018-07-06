""" 
	lambda functions are name less function

	use when we need sort throw away functions


"""


if __name__  ==  '__main__':

	name  =	lambda fn,ln: ln.strip().title()+" "+fn.strip().title() # title() changes first letter to upper case
	print(name("Sundar ","Bharath")) 