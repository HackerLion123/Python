import time
import asyncio

#ASYNCHRONOUS_CODE: Runs multiple functions seemingly in parallel.

#Requires cooporative, well-behaving functions

#Should not use blocking functions!


async def loading(break_point):
	print("loading.......")
	i = 1
	while True:
		if i%1000 == 0:
			print("({0}/{1})".format(i,break_point))
		if i == break_point:
			break
		time.sleep(0.001)
		#await asyncio.sleep(0.001)
		i += 1

async def main():

	await asyncio.wait([
		loading(10000)
		])
	

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
