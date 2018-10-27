
def no_of_ways(n,x):
	count = 0
	for step in x:
		if n%step == 0:
			count += 1
	return count

def main():
	n = int(input())
	x = [int(e)	for e in input().split()]
	print(no_of_ways(n,x))


if __name__ == '__main__':
	main()