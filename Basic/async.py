import time

#ASYNCHRONOUS_CODE: Runs multiple functions seemingly in parallel.

#Requires cooporative, well-behaving functions

#Should not use blocking functions!


def loading(break_point):
	print("loading.......")
	i = 0
	while True:
		if i%1000 == 0:
			print((i/break_point)*100)
		if i == break_point:
			break
		time.sleep(0.001)
		i += 1

def main():
	loading(10000)
if __name__ == '__main__':
	main()
