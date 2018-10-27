import numpy as np

def nPuzzle(n,inital,goal):
	#print("hello")
	count = 0
	x,y = -1,-1
	for i in range(n):
		for j in range(n):
			if inital[i][j] == 0:
				x,y = i,j
	if x == -1:
		raise ValueError("No free space to move")
	while cost(inital,goal) != 0:
		count += 1
		inital,x,y = move(n,x,y,inital,goal)
		print(inital)
	return count

def cost(inital,goal):
	c = 0
	for i in range(len(inital)):
			if inital[i][i] != goal[i][i]:
				if inital[i][i] == 0:
					pass
				c += 1
	return c

def move(n,x,y,inital,goal):
	""" 0-top 1-bottom 2-left 3-right"""
	#print(inital)
	temp = np.copy(inital)
	left,right,top,bottom = 1000,1000,1000,1000
	if x>=0:
		inital = np.copy(temp)
		inital[x-1][y],inital[x][y] = inital[x][y],inital[x-1][y] 
		top = cost(inital,goal)
		#print(inital)
	if y>=0:
		inital = np.copy(temp)
		inital[x][y-1],inital[x][y] = inital[x][y],inital[x][y-1] 
		left = cost(inital,goal) 
		#print(inital)
	if x<n-2:
		inital = np.copy(temp)
		inital[x+1][y],inital[x][y] = inital[x][y],inital[x+1][y] 
		bottom = cost(inital,goal)
		#print(inital)
	if y<n-2:
		inital = np.copy(temp)
		inital[x][y+1],inital[x][y] = inital[x][y],inital[x][y+1]
		right = cost(inital,goal) 
		#print(inital)
	inital = np.copy(temp)
	#print(left,right,top,bottom)
	num = min(top,left,right,bottom)
	if top == num:
		inital[x-1][y],inital[x][y] = inital[x][y],inital[x-1][y]
		return inital,x-1,y
	elif left == num:
		inital[x][y-1],inital[x][y] = inital[x][y],inital[x][y-1]
		return inital,x,y-1
	elif right == num:
		inital[x+1][y],inital[x][y] = inital[x][y],inital[x+1][y]
		return inital,x+1,y
	elif bottom == num:
		inital[x][y+1],inital[x][y] = inital[x][y],inital[x][y+1]
		return inital,x,y+1


def main():
	n = int(input())
	inital = np.zeros([n,n])
	goal = np.zeros([n,n])
	for i in range(n):
		for j in range(n):
			inital[i][j] = int(input())

	print("Goal State")
	for i in range(n):
		for j in range(n):
			goal[i][j] = int(input())
	print(nPuzzle(n,inital,goal))
	#print("Steps = " +str(nPuzzle(n,inital,goal)))

if __name__ == '__main__':
	main()