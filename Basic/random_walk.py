import random

""" 
	Random walk and Monte Carlo Prediction
	It predicts the number of times user need a transport to go home
	if the distance is more than 4 blocks then he need a transport.  
"""

def random_walk(n): 
	""" Returns the co-ordinates x and y """
	x,y  = 0,0
	for i in range(n):
		dx,dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)]) # [North,South,East,West]

		x += dx
		y += dy
	return x,y

def main():
	""" Does the Monte Carlo Prediction """

	number_of_walks = 10000

	for blocks in range(1,31):

		times_vechile_not_need = 0
		for n in range(1,number_of_walks):
			x,y	= random_walk(blocks)
			#print(x,y)
			distance = abs(x) + abs(y);
			#print(distance)
			if distance <= 4:
				times_vechile_not_need += 1
		percent = (times_vechile_not_need / 10000) * 100

		rand_points = [ random_walk(blocks) for n in range(1,number_of_walks)  ]
		distance = [ abs(x) + abs(y) ]
		print(rand_points)
		print("walk_count = {0} percentage = {1}%".format(blocks,percent))


if __name__ == '__main__':
	main()
