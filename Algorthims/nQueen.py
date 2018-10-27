import numpy as np

def nQueen(n):
	board = np.zeros([n,n])
	board = board.tolist()
	stack = []
	l = 0
	i = 0
	j = 0
	while i<n:
		while j<n:
			#print(canPlace(i,j,board,n))
			if canPlace(i,j,board,n)==True:
				board[i][j] = 'q'
				#print(board)
				stack.append((i,j))
				break
			j += 1
		i += 1
		if j == n:
			#print(j)
			x,y  = stack.pop()
			i,j,stack = Backtrack(x,y,board,n,stack)
		else:
			j = 0
	return board

def Backtrack(x,y,board,n,stack):
	if y == n-1:
		board[x][y] = 0.0
		y = 0
		if canPlace(x,y,board,n):
			return x,y,stack
		else:
			x,y = stack.pop()
			return Backtrack(x,y,board,n,stack)
	else:
		board[x][y] = 0.0
		y = y+1
		return x,y,stack

def canPlace(x,y,board,n):
	for i in range(x):
		if board[i][y] == 'q':
			return False
	for i in range(y):
		if board[x][i] == 'q':
			return False
	if x>y:
		for i in range(1,y+1):
			if board[x-i][y-i] == 'q':
				return False
	else:
		for i in range(1,x+1):
			if board[x-i][y-i] == 'q':
				return False
	for i in range(0,n-y):
		if board[x-i][y+i] == 'q':
			return False
	return True

def main():
	n = int(input())
	for ele in nQueen(n):
		print(ele)
	# board = [['q','',''],['','',''],['','','']]
	# print(canPlace(1,1,board,3))

if __name__ == '__main__':
	main()
