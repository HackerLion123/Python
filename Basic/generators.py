import time 

t1 = time.time()
for i in range(100000):
	i = i*i
t2 = time.time()
print("Time taken normally {}".format(t2-t1))

t1 = time.time()
gen = (x*x for x in range(100000))

for  g in gen:
	pass;
t2 = time.time()  
print("Generator took {}".format(t2-t1))

t1 = time.time()
list = [x*x for x in range(100000)]
t2 = time.time()
print("ListComprehension took {}".format(t2-t1))


def add_gen(num)
	"""Function that uses yield is a generator"""

	for i in range(num):
		yield i*i

def add(num):
	for i in range(num):
		pass;
